# 1,2 Member class의 속성 정의
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def add_member():
        Member.add_member(input("Enter name: "), input(
            "Enter username: "), input("Enter password: "))


# 5 Member instance 3개 만들기
member1 = Member("보라돌이", "purple", "eggplant1")
member2 = Member("뚜비", "green", "grass2")
member3 = Member("나나", "yellow", "banana3")

# 3 Member class에 회원정보를 print해주는 display
# (Member class의 메소드라고 부를 수 있는지는 모르겠다.)
print(member1.name, "'s username is ", member1.username)
print(member2.name, "'s username is ", member2.username)
print(member3.name, "'s username is ",  member3.username)

# 5 members 빈 리스트에 append써서 회원 인스턴스 저장
members = []
members.append(member1)
members.append(member2)
members.append(member3)
print("Name of the members are",
      members[0].name, members[1].name, members[2].name)

# 1,4 Post class의 속성 정의


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# 6 posts instance 3개 만들기
post1 = Post("오늘아침메뉴", "빵먹었다", member1.username)
post2 = Post("어제점심메뉴", "김밥먹었다", member2.username)
post3 = Post("어제저녁메뉴", "생선먹었다", member3.username)

# 6 posts 빈 리스트에 append써서 게시글 인스턴스 저장 / 제목 프린트 / 특정단어가 포함된 게시글의 제목 프린트
posts = []
posts.append(post1)
posts.append(post2)
posts.append(post3)
for t in posts:
    print(t.author, "posted", t.title)
for t2 in posts:
    if '먹었다' in posts:
        print(t2.content)  # error
