# import libraries
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# ortam değişkenlerini tanımla

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# LLM + Memory
# büyük dil modeli
llm = ChatOpenAI(
    model = "gpt-4.1-nano-2025-04-14", # kullandığımız model adı
    temperature = 0.7, #0-1 arası değerler alır. 0'a yakınsa garanti cevap, 1'e yakınsa daha çok düşünür. 1'e yakınlaştıkça halisünasyon riski artar.
    openai_api_key = api_key
)

# hafıza özelliği
memory = ConversationBufferMemory(return_messages=True)


conversation = ConversationChain(llm = llm, memory = memory, verbose = True)


# kullanıcı bilgilerini al, isim ve yaş

name = input("Adınız: ")
age = input("Yaşınız: ")

intro = (
    f"Sen bir doktor asistanısın. Hasta {name}, {age} yaşında. "
    "Sağlık sorunları hakkında konuşmak istiyor. " 
    "Yaşına uygun dikkatli ve uygun tavsiyeler ver; ismiyle hitap et."

)


memory.chat_memory.add_user_message(intro)

print("Merhaba ben bir doktor asistanıyım, size nasıl yardımcı olabilirim.")


# chatbot döngüsü tanımla
while True:
    # hasta soru sordu
    user_msg = input(f"{name}: ")
    if user_msg.lower() == "quit":
        print("Görüşmek üzere...") # konuşmayi sonlandir.
        break

# doktor asistanı cevap verdi ve hafizaya atildi
    reply = conversation.predict(input = user_msg) # llm cevabi
    print(f"Doktor asistanı: {reply}")

# verilen cevaplari memory'e kaydet. (memory'i görüntüleyebilmek için)
    print("Hafiza: ")
    for idx, m in enumerate(memory.chat_memory.messages, start= 1):
        print(f"{idx:02d}. {m.type.upper()}: {m.content}")
    print("----------------------------\n")