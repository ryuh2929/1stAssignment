import hashlib
import secrets


class Member:
    def __init__(self, name, username, password):
        salt = '소금냠냠' + secrets.token_hex(8)
        self.name = name
        self.username = username
        self.password = hashlib.sha512(password+salt.encode()).hexdigest()

    def __str__(self):
        return f'name : {self.name}, username : {self.username}, password : {self.password}'

    def display(self):
        print(f'name : {self.name} / username : {self.username}')


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f'title : {self.title}, content : {self.content}, author : {self.author}'


members = []

member1 = Member('John', 'jsmith123', 'password123')
member2 = Member('Alice', 'alice_s', 'secret123')
member3 = Member('David', 'd.jvid', 'securepass')

members.append(member1)
members.append(member2)
members.append(member3)

for a in members:
    Member.display(a)

posts = []

post1_1 = Post('점메추', '받는다', members[0].username)
post1_2 = Post('오점벅', '오늘 점심 버거라는 뜻', members[0].username)
post1_3 = Post('햄최몇?', '일단 난 5개', members[0].username)
post2_1 = Post('오운완', '핑크덤벨 3회ㅇㅅㅇ', members[1].username)
post2_2 = Post('운동 너무 열심히 한거 같다', '알베겨서 힘들다', members[1].username)
post2_3 = Post('운동 너무 열심히해서 근육몬되면 어떡함?',
               '적당히 마른 근육만 만들고 싶은데ㅇㅅㅇ', members[1].username)
post3_1 = Post('ㅇㅅㅇ', '뭐ㅇㅅㅇ', members[2].username)
post3_2 = Post('누르지 마시오', '이번만 봐드리는 겁니다', members[2].username)
post3_3 = Post('댓글창 레전드ㅋㅋ', '왔으면 불끄고가', members[2].username)

posts.append(post1_1)
posts.append(post1_2)
posts.append(post1_3)
posts.append(post2_1)
posts.append(post2_2)
posts.append(post2_3)
posts.append(post3_1)
posts.append(post3_2)
posts.append(post3_3)

for a in posts:
    user1 = members[0].username
    if a.author == user1:
        print(f'{user1}이 작성한 글제목: {a.title}')

for a in posts:
    text = 'ㅇㅅㅇ'
    if text in a.content:
        print(f'{text}가 내용에 포함된 글제목: {a.title}')

