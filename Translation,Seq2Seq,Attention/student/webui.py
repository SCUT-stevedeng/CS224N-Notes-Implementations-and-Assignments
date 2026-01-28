#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gradio Web UI for Machine Translation
"""

import gradio as gr
import torch
import sentencepiece as spm
import sys
from typing import List
from nmt_model import NMT, Hypothesis

# Global variables for model and sentencepiece processor
model = None
sp_processor = None
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def load_model(model_path: str):
    """Load the translation model"""
    global model
    try:
        print(f"Loading model from {model_path}...", file=sys.stderr)
        model = NMT.load(model_path)
        model = model.to(device)
        model.eval()
        print("Model loaded successfully!", file=sys.stderr)
        return "模型加载成功！"
    except Exception as e:
        error_msg = f"模型加载失败: {str(e)}"
        print(error_msg, file=sys.stderr)
        return error_msg


def process_text(text: str) -> List[List[str]]:
    """Process input text using SentencePiece"""
    global sp_processor
    if sp_processor is None:
        sp_processor = spm.SentencePieceProcessor()
        sp_processor.load('src.model')
    
    # Split text into lines and process each line
    lines = text.strip().split('\n')
    data = []
    for line in lines:
        if line.strip():
            subword_tokens = sp_processor.encode_as_pieces(line)
            data.append(subword_tokens)
    return data


def translate_text(source_text: str, model_path: str) -> str:
    """Translate source text to target language"""
    global model
    
    if not source_text.strip():
        return "请输入要翻译的文本"
    
    # Load model if not loaded or if path changed
    if model is None or (hasattr(translate_text, 'last_model_path') and translate_text.last_model_path != model_path):
        load_result = load_model(model_path)
        if "失败" in load_result:
            return load_result
        translate_text.last_model_path = model_path
    
    try:
        # Process input text
        test_data_src = process_text(source_text)
        
        if not test_data_src:
            return "无法处理输入文本"
        
        # Translate using beam search
        hypotheses = []
        beam_size = 10
        max_decoding_time_step = 70
        
        with torch.no_grad():
            for src_sent in test_data_src:
                example_hyps = model.beam_search(
                    src_sent, 
                    beam_size=beam_size, 
                    max_decoding_time_step=max_decoding_time_step
                )
                hypotheses.append(example_hyps)
        
        # Format output
        results = []
        for hyps in hypotheses:
            top_hyp = hyps[0]
            hyp_sent = ''.join(top_hyp.value).replace('▁', ' ')
            results.append(hyp_sent)
        
        return '\n'.join(results)
    
    except Exception as e:
        error_msg = f"翻译出错: {str(e)}"
        print(error_msg, file=sys.stderr)
        return error_msg


# Initialize translate_text attribute
translate_text.last_model_path = None

# Create Gradio interface
def create_interface():
    with gr.Blocks(title="机器翻译系统") as demo:
        gr.Markdown("# 机器翻译系统")
        gr.Markdown("输入源语言文本，点击翻译按钮即可获得翻译结果")
        
        with gr.Row():
            with gr.Column():
                model_path_input = gr.Textbox(
                    label="模型路径 (Model Path)",
                    placeholder="例如: model.bin",
                    value="model.bin"
                )
                source_text = gr.Textbox(
                    label="源语言文本 (Source Text)",
                    placeholder="请输入要翻译的文本...",
                    lines=10
                )
                translate_btn = gr.Button("翻译 (Translate)", variant="primary")
            
            with gr.Column():
                target_text = gr.Textbox(
                    label="翻译结果 (Translation Result)",
                    lines=10,
                    interactive=False
                )
        
        translate_btn.click(
            fn=translate_text,
            inputs=[source_text, model_path_input],
            outputs=target_text
        )
        
        gr.Examples(
            examples=[["Hello, how are you?", "model.bin"]],
            inputs=[source_text, model_path_input]
        )
    
    return demo


if __name__ == "__main__":
    demo = create_interface()
    demo.launch(share=False, server_name="127.0.0.1", server_port=7860)