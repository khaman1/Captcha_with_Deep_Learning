import requests

for i in range(1,10000):
    print(i)
    r = requests.get('http://tracuunnt.gdt.gov.vn/tcnnt/captcha.png?uid=f72c1ab9-49e8-432a-be9d-a2f71826a4ff')  
    with open(r'data4len4digit/train/'+str(i)+'.png', 'wb') as f:
        f.write(r.content)
