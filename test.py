from pyht import Client
from dotenv import load_dotenv
from pyht.client import TTSOptions
import os
load_dotenv()

client = Client(
    user_id=os.getenv("qMpf0bdcnLbcVwZ7yeAF8y2YfSl1"),
    api_key=os.getenv("25ae75c26dc9440a83774251557b648c"),
  
  	# for on-prem users, uncomment and add the advanced grpc_addr option below. Replace grpc_addr with your endpoint. 
  	# advanced=client.Client.AdvancedOptions(grpc_addr="{your-endpoint}.on-prem.play.ht:11045")
)
options = TTSOptions(voice="s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json")
for chunk in client.tts("Can you tell me your account email or, ah your phone number?", options):
    # do something with the audio chunk
    print(type(chunk))