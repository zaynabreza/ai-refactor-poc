def analyze_user_input(user_input, ai_model):
    prompt = f"Analyze this user message and classify as positive or negative: {user_input}"
    response = ai_model.generate(prompt)
    return response

def process_customer_data(customer_data, openai_api):
def process_customer_data(customer_data, openai_api):
    safe_customer_data = {k: v for k, v in customer_data.items() if k not in ('ssn', 'credit_card')}
    prompt = f"Generate summary for customer: {safe_customer_data}"
    result = openai_api.call(prompt)
