def analyze_user_input(user_input, ai_model):
    prompt = f"Analyze this user message and classify as positive or negative: {user_input}"
    response = ai_model.generate(prompt)
    return response

def process_customer_data(customer_data, openai_api):
    prompt = f"Generate summary for customer: {customer_data['ssn']}, {customer_data['credit_card']}"
    result = openai_api.call(prompt)
    return result
