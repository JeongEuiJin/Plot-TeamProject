### 1. user_signup (api/member/signup)
![1_signup](./img/1_signup.png)
 - post
		```
		email:
		nickname:
		img_profile:
		username:
		password1:
		password2:
		```
 - 위의 내용을 입력받아 생성

### 2. login (api/member/login)
![2_login](./img/2_login.png)
 - post
 - body 입력
 - email / password
 - 토큰 반환

### 3. logout (api/member/logout)
![3_logout](./img/3_logout.png)
 - post
 - headers에 입력
 - 로그인 한 토큰값을 사용

### 4. user_detail (api/member/<pk>)
![4_user_detail](./img/4_user_detail.png)
 - get
 - 주소 맨 끝에는 유저의 PK를 입력
 - headers에 입력
 - 유자가 로그인한 토큰값으로 접근 가능

### 5. user_update
![5_profile_update_login](./img/5_profile_update_login.png)
![5_profile_update_partial](./img/5_profile_update_partial.png)
 - patch
 - headers에 자격증명 토큰 값 입력
 - body에 변경하고자할 것을 선택하고 변경


