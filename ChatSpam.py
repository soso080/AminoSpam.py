import aminoboi
import concurrent.futures
import os

os.system("clear")
print("""
╭━━━┳╮╱╱╱╱╭╮
┃╭━╮┃┃╱╱╱╭╯╰╮
┃┃╱╰┫╰━┳━┻╮╭╯
┃┃╱╭┫╭╮┃╭╮┃┃
┃╰━╯┃┃┃┃╭╮┃╰╮
╰━━━┻╯╰┻╯╰┻━╯
╭━━━╮╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╭╯╰╮
┃╰━━┳━━┳━┳┳━┻╮╭╯
╰━━╮┃╭━┫╭╋┫╭╮┃┃
┃╰━╯┃╰━┫┃┃┃╰╯┃╰╮
╰━━━┻━━┻╯╰┫╭━┻━╯
╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╰╯
""")
print('\033[1;36mFeito por ~>\033[1;92m Moleey\n')
client = aminoboi.Client()
email = str(input("\033[1;36memail: \033[0m"))
senha = str(input("\033[1;92msenha: \033[0m"))
client.auth(email=email, password=senha)

get =client.get_from_link(str(input("\033[1;36mLink: \033[0m")))
thread_Id= get["linkInfoV2"]["extensions"]["linkInfo"]["objectId"]
ndc_Id=get["linkInfoV2"]["extensions"]["linkInfo"]["ndcId"]
print(f"\n{thread_Id} >> {ndc_Id}\n")

message = str(input("\033[1;92mSua mensagem: \033[0m"))
message_type = str(input("\033[1;36mMensagemType: \033[0m"))


while True:
	print("\033[1;92mSpamando o chat")
	with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
	                   	_ = [
	                   	executor.submit(
	                   	client.send_message,
	                   	ndc_Id,
	                   	thread_Id,
	                   	message,
	                   	message_type
	                   	) for _ in range(100000)]