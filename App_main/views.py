from django.shortcuts import render, redirect
from .forms import UserProfileForm
import openai


openai.api_key = 'your open api key here'


# Create your views here.
def home(request):
    user_profile = None  # Initialize user_profile to None

    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            user_profile = form.save(commit=False)

            # Use OpenAI GPT-3 for text generation (chat-based model)
            prompt = f"Customize my resume to highlight and emphasize my strong technical skills, ensuring they align seamlessly with the specific requirements of the job post. Maintain the integrity and accuracy of my original resume, focusing on making it outstanding and relevant to capture the attention of human resources. Emphasize key technical expertise while ensuring the customized content reflects the truthfulness of my skills and experiences:\n\nResume: {user_profile.resume}\n\nJob Post: {user_profile.job_post}\n\n"
            messages = [
                {"role": "system", "content": "You are a helpful and a knowledgable about resume customization assistant."},
                {"role": "user", "content": prompt},
            ]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500
            )

            user_profile.customized_resume = response['choices'][0]['message']['content']
            user_profile.save()

            print("Customized Resume:", user_profile.customized_resume)  #for debugging purpose
            print("done with 500 tokens") #debugging
    else:
        form = UserProfileForm()

    return render(request, 'App_main/home.html', {'form': form, 'user_profile': user_profile})




def contact(request):
    return render(request, 'App_main/contact.html')



