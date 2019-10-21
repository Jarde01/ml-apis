import hug
import torch
from transformers import *

tokenizer = TransfoXLTokenizer.from_pretrained('transfo-xl-wt103')
model = TransfoXLLMHeadModel.from_pretrained('transfo-xl-wt103')


@hug.post("/generate")  # noqa
def transformer_generate(prompt: hug.types.text = "Test text", num_tokens: hug.types.number = 10, hug_timer=10):
    print(f"Original prompt: {prompt}")
    print(f"Tokens to generate: {num_tokens}")

    line_tokenized = tokenizer.tokenize(prompt)
    line_indexed = tokenizer.convert_tokens_to_ids(line_tokenized)
    tokens_tensor = torch.tensor([line_indexed])
    # tokens_tensor = tokens_tensor.to(device)

    predicted_tokens = []
    max_predictions = num_tokens
    mems = None
    for i in range(max_predictions):
        predictions, mems = model(tokens_tensor, mems=mems)
        predicted_index = torch.topk(predictions[0, -1, :], 5)[1][1].item()
        predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
        print(predicted_token)
        predicted_tokens.append(predicted_token)
    #     predicted_index = torch.tensor([[predicted_index]]).to(device)
        predicted_index = torch.tensor([[predicted_index]])
        tokens_tensor = torch.cat((tokens_tensor, predicted_index), dim=1)

    predicted_sentence = " ".join(predicted_tokens)

    return {"prompt": prompt,
            "generated_sentence": predicted_sentence,
            'took': float(hug_timer)}
