import os
from aiohttp import web
from transformers import AutoModelForCausalLM, AutoTokenizer


async def call_test(request):
	content = "ok"
	return web.Response(text=content,content_type="text/html")


async def call_gpt(request):

    # chat_history = "|0|1|What weather do you like?|1|1|Sunny.|0|1|Do you ready for walk?"
    chat_history = str(await request.text()).replace('\ufeff', '')    
    bot_input_ids = tokenizer.encode(chat_history + tokenizer.eos_token, return_tensors='pt')
    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(
        bot_input_ids, 
        max_length=1000, 
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=100,
        top_p=0.9,
        temperature=0.6,
        device=os.environ.get('DEVICE', ''),
        mask_token_id=tokenizer.mask_token_id,
        eos_token_id=tokenizer.eos_token_id,
        unk_token_id=tokenizer.unk_token_id,
    )
    # last ouput tokens from bot
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    return web.Response(text=response,content_type="text/html")


def main():

	app = web.Application(client_max_size=1024**3)
	app.router.add_route('GET', '/test', call_test)
	app.router.add_post('/gpt', call_gpt)

	web.run_app(
		app,
		port=os.environ.get('PORT', ''),
	)


tokenizer = AutoTokenizer.from_pretrained(os.environ.get('MODEL', ''))
model = AutoModelForCausalLM.from_pretrained(os.environ.get('MODEL', ''))

if __name__ == "__main__":
    main()
