import discord
import asyncio
import random
import os
import datetime
from time import sleep
import arrow
from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope1 = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] #정책시트
scope2 = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] #재고시트
scope3 = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] #재고시트
creds1 = ServiceAccountCredentials.from_json_keyfile_name('dongpan-699a93059b16.json', scope1) #정책시트
creds2 = ServiceAccountCredentials.from_json_keyfile_name('jumun-8151173be58f.json', scope2) #재고시트
creds3 = ServiceAccountCredentials.from_json_keyfile_name('dongpan-699a93059b16.json', scope3) #재고시트
client1 = gspread.authorize(creds1) #정책시트
client2 = gspread.authorize(creds2) #재고시트
client3 = gspread.authorize(creds3) #재고시트
doc1 = client1.open_by_url('https://docs.google.com/spreadsheets/d/1hL4uvq2On11zp-_JWoWMG0Gyyuty5Lhvp_gQkfTYsOI') #정책시트
doc2 = client2.open_by_url('https://docs.google.com/spreadsheets/d/15p6G4jXmHw7Z_iRCYeFwRzkzLxqf-3Pj0c6FeVuFYBM') #재고시트
doc3 = client3.open_by_url('https://docs.google.com/spreadsheets/d/18-a0Upet-wmPWTcymSMfzNzQzrYd1u43SNeeYLfrcgM') #디메릿시트


client = discord.Client()


@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='업무지원', type=1))

@client.event
async def on_member_join(member):
    sleep(1)	
    fmt = '{1.name} 에 오신것을 환영합니다.\n{0.mention} 님!! \n매장이름/직급/성함/연락처 이렇게 남겨주시면 \n확인후 권한을 승인해드리겠습니다. '
    channel = member.server.get_channel("661832869521391646")
    return await client.send_message(channel, fmt.format(member, member.server))


@client.event
async def on_message(message):
    
          
	if message.content.startswith('!동판'):
		SearchID = message.content[len('!동판')+1:]
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('정책표관리').worksheet('동판출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		embed1 = discord.Embed(
			title = ' :globe_with_meridians:  ' + SearchID + ' 안내 ',
			description= '**```css\n' + SearchID + ' 정책입니다. ' + result + ' ```**',
			color=0x00ffff
			)
		embed2 = discord.Embed(
			title = ' :globe_with_meridians: 동판 ' + SearchID + ' 정책조회!! ',
			description= '```' "출력자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
			color=0x00ffff
			)
		await client.send_message(client.get_channel("674653007132229632"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
	if message.content.startswith('!디메릿'):
		SearchID = message.content[len('!디메릿')+1:]
		gc3 = gspread.authorize(creds3)
		wks = gc3.open('디메릿관리').worksheet('디메릿출력')
		wks2 = gc3.open('디메릿관리').worksheet('디메릿금액정리')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		result2 = wks2.acell('B2').value
		
		embed1 = discord.Embed(
			title = ' 적용일시: ' + result2 + ' 디메릿 안내 ',
			description= '**```css\n' + SearchID + '' + result + ' ```**',
			color=0x4BAF4B
			)
		embed2 = discord.Embed(
			title = SearchID + ' 디메릿 조회!! ',
			description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + '```',
			color=0x4BAF4B
			)
		await client.send_message(client.get_channel("687385604396417079"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)		
		
		
		
		
	if message.content.startswith('!공짜폰'):
		SearchID = message.content[len('!공짜폰')+1:]
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('정책표관리').worksheet('무선공짜출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		
		embed1 = discord.Embed(
			title = ' 오늘의 ' + SearchID + ' 공짜폰 안내 ',
			description= '**```css\n' + SearchID + '  정책입니다. ' + result + ' ```**',
			color=0x4BAF4B
			)
		embed2 = discord.Embed(
			title = SearchID + ' 공짜폰 조회!! ',
			description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + '```',
			color=0x4BAF4B
			)
		await client.send_message(client.get_channel("674652501693300737"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
		
		
	if message.content.startswith('!외국인공짜폰'):
		SearchID = message.content[len('!외국인공짜폰')+1:]
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('정책표관리').worksheet('외국인공짜출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		
		embed1 = discord.Embed(
			title = ' 오늘의 ' + SearchID + ' 외국인공짜폰 안내 ',
			description= '**```css\n' + SearchID + '  정책입니다. ' + result + ' ```**',
			color=0xFF848F
			)
		embed2 = discord.Embed(
			title = SearchID + ' 외국인공짜폰 조회!! ',
			description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
			color=0xFF848F
			)
		await client.send_message(client.get_channel("674654114592063498"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
	if message.content == '!정책표':
		command_list = ''
		command_list += '\n'
		command_list += '📌 공지사항\n'
		command_list += '```css\n⭕2020-02-18기준 부터\n⭕방x위 지시사항으로 정책표상에 [시간기재가 금지]됩니다.\n⭕정책적용기준은 정책표 제목시간 확인바랍니다.\n⭕폰클단가표 보는법은\n⭕정책표 왼편상단 보안코드란에 [매장P코드] 넣어주시고\n⭕[P는 대문자]이어야 하고 뒤에 [0세개는 빼주세요.]\n⭕그레이드확인은 [!그레이드] 로 확인 가능하십니다..\n⭕장기고객 기변프로모션은 [!비하인드] 로 확인 가능하십니다..\n⭕가족결합정책 종료!! ```'
		command_list += '\n'
		command_list += '폰클사이트 링크\n'
		command_list += 'https://shop.poncle.co.kr/?action=login&url=Lw== \n'     #!링크
		command_list += '\n'
		command_list += ''
		command_list += ''
		command_list += ''     #!링크
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('정책표관리').worksheet('무선구두')
		result = wks.acell('E3').value
		embed1 = discord.Embed(
			title = '정책표 안내',
			description= command_list,
			color=0xf29886
			)
		embed2 = discord.Embed(
			title = '폰클링크안내!',
			description= '```\n출력자:' + message.author.display_name +'\n거래처:' + message.channel.name + '```',
			color=0xf29886
			)
		await client.send_message(client.get_channel("672022974223876096"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
	if message.content.startswith('!그레이드'):
		gc2 = gspread.authorize(creds2)
		wks = gc2.open('재고관리').worksheet('그레이드')
		result = wks.acell('B1').value
		embed1 = discord.Embed(
			title = ' 파트너 그레이드 안내!! ',
			description= '**```css\n' + result + ' ```**',
			color=0x7fffd4
			)
		embed2 = discord.Embed(
			title = ' 파트너 그레이드 조회!! ',
			description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
			color=0x00ffff
			)
		await client.send_message(message.channel, embed=embed1)
		await client.send_message(client.get_channel("674827771817623572"), embed=embed2)
		
	if message.content.startswith('!주문'):
		curruntTime = datetime.datetime.now() + datetime.timedelta(hours = 9)
		krnow = curruntTime.strftime('%Y/%m/%d %H:%M')
		gc2 = gspread.authorize(creds2)
		wks = gc2.open('재고관리').worksheet('디스코드주문내역')
		wks.insert_row([krnow, message.channel.name, message.author.display_name, message.content[4:]], 3)
		embed1 = discord.Embed(
			title = message.author.display_name + "님 의 주문 ",
			description= '```fix\n' + message.content[4:] + '```',
			color=0xCBFF75
			)
		embed1.add_field(
			name=" 주문접수 확인... ",
			value= '```diff\n!주문내용이 전달되어 정상적으로\n!접수되었습니다. 부득이한경우\n!개인답변 드리겠습니다.```'
			)
		embed2 = discord.Embed(
			title = message.author.display_name + "님 의 주문내용 ",
			description= '```' + message.content[4:] + '```',
			color=0xCBFF75
			)
		embed2.add_field(
			name=" 주문 접수처... ",
			value= '```' "거래처:"+ message.channel.name +"\n채널아이디:" + message.channel.id + '```'
			)
		await client.send_message(message.channel, embed=embed1)
		await client.send_message(client.get_channel("667343258296254464"), embed=embed2)
		
	if message.content.startswith('!답변'):
		member = discord.utils.get(client.get_all_channels(), id=message.content[4:22])
		neyongdabtotal = message.content[23:]
		neyongdab = neyongdabtotal.split("/")
		neyong = neyongdab[0]
		dab = neyongdab[1]
		
		embed = discord.Embed(
			title = "주문내용",
			description= '```fix\n' + neyong + '```',
			color=0xFF0000
			)
		embed.add_field(
			name = message.author.display_name + "님 답변",
			value= '```Tex\n' + '$' + dab + '```'
			)
		await client.send_message(member, embed=embed)
		

	if message.content.startswith('!공지'):
		if message.author.id == '315237238940106754' :
			embed = discord.Embed(    
				title = "📌 공지사항",
				description= '```' + message.content[4:] + '```',
				color=0xFF0000	
				)
			await client.send_message(client.get_channel("667707237623660569"), embed=embed)
			await client.send_message(client.get_channel("667239441307533312"), embed=embed)
			await client.send_message(client.get_channel("667241204739604490"), embed=embed)
			await client.send_message(client.get_channel("667241430070198273"), embed=embed)
			await client.send_message(client.get_channel("667241481907470336"), embed=embed)
			await client.send_message(client.get_channel("667241531694120970"), embed=embed)
			await client.send_message(client.get_channel("667241582411513856"), embed=embed)
			await client.send_message(client.get_channel("667241378534653983"), embed=embed)
			await client.send_message(client.get_channel("667240616207450122"), embed=embed)
			await client.send_message(client.get_channel("667242915378102293"), embed=embed)
			await client.send_message(client.get_channel("667243361614168088"), embed=embed)
			await client.send_message(client.get_channel("667243407227224064"), embed=embed)
			await client.send_message(client.get_channel("667243524433117218"), embed=embed)
			await client.send_message(client.get_channel("667247020926435344"), embed=embed)
			await client.send_message(client.get_channel("667243630989410304"), embed=embed)
			await client.send_message(client.get_channel("667243696915218432"), embed=embed)
			await client.send_message(client.get_channel("667243782604849155"), embed=embed)
			await client.send_message(client.get_channel("667243837206429696"), embed=embed)
			await client.send_message(client.get_channel("667244790404087808"), embed=embed)
			await client.send_message(client.get_channel("667244947677904898"), embed=embed)
			await client.send_message(client.get_channel("667245023359664142"), embed=embed)
			await client.send_message(client.get_channel("667245114619592765"), embed=embed)
			await client.send_message(client.get_channel("667245155790618625"), embed=embed)
			await client.send_message(client.get_channel("667245231447474176"), embed=embed)
			await client.send_message(client.get_channel("667245522549211138"), embed=embed)
			await client.send_message(client.get_channel("667245576014004256"), embed=embed)
			await client.send_message(client.get_channel("667245650802507777"), embed=embed)
			await client.send_message(client.get_channel("667245748907147275"), embed=embed)
			await client.send_message(client.get_channel("667245819786690560"), embed=embed)
			await client.send_message(client.get_channel("667245916947742760"), embed=embed)
			await client.send_message(client.get_channel("667246076453191690"), embed=embed)
			await client.send_message(client.get_channel("667246146074443807"), embed=embed)
			await client.send_message(client.get_channel("667246234851082240"), embed=embed)
			await client.send_message(client.get_channel("667246316652593163"), embed=embed)
			await client.send_message(client.get_channel("667246366468079626"), embed=embed)
			await client.send_message(client.get_channel("667246430074699777"), embed=embed)
			await client.send_message(client.get_channel("667246487872339968"), embed=embed)
			await client.send_message(client.get_channel("667246552238129153"), embed=embed)
			await client.send_message(client.get_channel("667246600019771472"), embed=embed)
			await client.send_message(client.get_channel("667246718198218772"), embed=embed)
			await client.send_message(client.get_channel("667246834892144640"), embed=embed)
			await client.send_message(client.get_channel("667247069580492820"), embed=embed)
			await client.send_message(client.get_channel("667247107232628736"), embed=embed)
			await client.send_message(client.get_channel("667247142833881108"), embed=embed)
			await client.send_message(client.get_channel("667247180188483584"), embed=embed)
			await client.send_message(client.get_channel("667247225847545866"), embed=embed)
			await client.send_message(client.get_channel("667247261734141962"), embed=embed)
			await client.send_message(client.get_channel("667247287679975446"), embed=embed)
			await client.send_message(client.get_channel("667247313525407755"), embed=embed)
			await client.send_message(client.get_channel("667247368902672404"), embed=embed)
			await client.send_message(client.get_channel("667247397075681299"), embed=embed)
			await client.send_message(client.get_channel("667247433041838100"), embed=embed)
			await client.send_message(client.get_channel("667247472908828676"), embed=embed)
			await client.send_message(client.get_channel("667247519264407552"), embed=embed)
			await client.send_message(client.get_channel("667247545893781524"), embed=embed)
		
		
	if message.content == '!명령어':
		command_list = ''
		command_list += '!명령어\n'     #!명령어
		command_list += '!모델명\n'     #!모델명
		
		embed = discord.Embed(
			title = ":keyboard: 기본명령어",
			description= '```fix\n' + command_list + '```',
			color=0xFFD5B4
			)
		embed.add_field(
			name="📶 정책관련 명령어 ",
			value= '```diff\n- !정책표\n- !끝단가\n- !외국인끝단가\n- !그레이드\n- !비하인드\n---< 비하인드 명령어는 음성지원만 확인가능합니다. >\n+ !단가 모델명 요금제군 유형\n---< ex)!단가 N976 A군 MNP >\n+ !외국인단가 모델명 요금제군 유형\n---< ex)!외국인단가 N976 A군 MNP >\n+ !공짜폰 요금제군 유형\n---< ex)!공짜폰 C군 MNP >\n+ !외국인공짜폰 요금제군 유형\n---< ex)!외국인공짜폰 A군 신규 > ```',
			inline = False
			)
		embed.add_field(
			name="📲 재고관련 명령어 ",
			value= '```diff\n- !주문\n---< ex)!주문 N976 화이트 1대 보내주세요 >\n+ !재고 모델명\n---< ex)!재고 N976 >\n+ !재고 [구단위]\n---< ex)!재고 남동구 >\n+ !퀵비 [동단위/동단위]\n---< ex)!퀵비 논현동/가좌동 >\n\n퀵비 멍령어는 실행은 되지만\n데이터량이 많아 다소 결과가 늦게 나옴 ```',
			inline = False
			)
		embed.add_field(
			name="🌐 동판관련 명령어 ",
			value= '```Cs\n# !동판 동판\n'+'@ !동판 소호신규\n@ !동판 소호기변\n@ !동판 후결합\n@ !동판 재약정\n@ !동판 재약정단독\n@ !동판 단독\n\n\n\n ```',
			inline = True
			)
		embed.add_field(
			name="🎲 기타 명령어 ",
			value= '```diff\n= !영화순위\n= !주사위\n= !복권\n+ !나이 생년-월-일 \n---< ex)!나이 2002-02-01 >\n+ !유지기간 개통일\n---< ex)!유지기간 2020-01-01 >\n+ !사다리 뽑을인원수 인원1 인원2 인원3...\n---< ex)!사다리 2 홍길동 갑돌이 갑순이 >\n+ !타이머 초시간\n---< ex)!타이머 5 >```',
			inline = True
			)
		await client.send_message(message.channel, embed=embed)
        
	if message.content == '!영업명령어':
		command_list = ''
		command_list += '!영업명령어\n'     #!명령어        
		command_list += '!모델명\n'     #!모델명
		command_list += '!거래처\n'     #!모델명
		
		embed = discord.Embed(
			title = "🚗 영업부 기본명령어",
			description= '```fix\n' + command_list + '```',
			color=0xFFD5B4
			)
		embed.add_field(
			name="📈 실적관련 명령어 ",
			value= '```diff\n- !전월실적\n---< 전월 전체실적 >\n+ !전월실적 영업사원이름\n---< ex)!전월실적 홍길동 >\n- !당월실적\n---< 데이터 입력일까지 당월 전체실적 >\n+ !당월실적 영업사원이름\n---< ex)!당월실적 홍길동 >\n\n실적 멍령어는 실행은 되지만\n데이터량이 많아 다소 결과가 늦게 나옴 ```',
			inline = False
			)
		embed.add_field(
			name="📶 정책관련 명령어 ",
			value= '```diff\n- !정책표\n- !끝단가\n- !외국인끝단가\n- !그레이드\n- !비하인드\n---< 비하인드 명령어는 음성지원만 확인가능합니다. >\n+ !단가 모델명 요금제군 유형\n---< ex)!단가 N976 A군 MNP >\n+ !외국인단가 모델명 요금제군 유형\n---< ex)!외국인단가 N976 A군 MNP >\n+ !공짜폰 요금제군 유형\n---< ex)!공짜폰 C군 MNP >\n+ !외국인공짜폰 요금제군 유형\n---< ex)!외국인공짜폰 A군 신규 > ```',
			inline = False
			)
		embed.add_field(
			name="📲 재고관련 명령어 ",
			value= '```diff\n- !주문\n---< ex)!주문 A305 A505 배정부탁드립니다. >\n+ !재고 모델명\n---< ex)!재고 N976 >\n+ !재고 거래처코드\n---< ex)!재고 A34 >\n- !불량\n---< 전체불량현황 >\n+ !불량 거래처코드\n---< ex)!불량 A34 >\n- !유심\n---< 10개 미만 유심현황 >\n+ !유심 전체\n---< 거래처 총 유심현황 >\n+ !퀵비 [동단위/동단위]\n---< ex)!퀵비 논현동/가좌동 >\n\n퀵비 멍령어는 실행은 되지만\n데이터량이 많아 다소 결과가 늦게 나옴 ```',
			inline = False
			)
		embed.add_field(
			name="🌐 동판관련 명령어 ",
			value= '```Cs\n# !동판 동판\n'+'@ !동판 소호신규\n@ !동판 소호기변\n@ !동판 후결합\n@ !동판 재약정\n@ !동판 재약정단독\n@ !동판 단독\n\n\n\n ```',
			inline = True
			)
		embed.add_field(
			name="🎲 기타 명령어 ",
			value= '```diff\n= !영화순위\n= !주사위\n= !복권\n+ !나이 생년-월-일 \n---< ex)!나이 2002-02-01 >\n+ !유지기간 개통일\n---< ex)!유지기간 2020-01-01 >\n+ !사다리 뽑을인원수 인원1 인원2 인원3...\n---< ex)!사다리 2 홍길동 갑돌이 갑순이 >\n+ !타이머 초시간\n---< ex)!타이머 5 >```',
			inline = True
			)
		await client.send_message(message.channel, embed=embed)		
		
	if message.content.startswith('!나이'):
		SearchID = message.content[len('!나이')+1:]
		gc2 = gspread.authorize(creds2)
		wks = gc2.open('재고관리').worksheet('만나이계산기')
		
		wks.update_acell('C8', SearchID)
		result1 = wks.acell('H8').value
		result2 = wks.acell('J8').value
		
		embed = discord.Embed(
			title = ' 오늘기준 ' + SearchID + ' 나이! ',
			description= '```css\n' + SearchID + result1 + result2 + '```',
			color=0x5ABEFF
			)
		await client.send_message(message.channel, embed=embed)
		
		
	if message.content.startswith('!유지기간'):
		SearchID = message.content[len('!유지기간')+1:]
		gc2 = gspread.authorize(creds2)
		wks = gc2.open('재고관리').worksheet('유지기간')
		wks.update_acell('a1', SearchID)
		result = wks.acell('b1').value
		
		embed = discord.Embed(
			title = ' 오늘기준 ' + SearchID + ' 개통자 남은 유지일수는 ',
			description= '```md\n' + SearchID + result + '```',
			color=0x5ABEFF
			)
		await client.send_message(message.channel, embed=embed)		
		
	if message.content.startswith('!영화순위'):
        # http://ticket2.movie.daum.net/movie/movieranklist.aspx
		i1 = 0 # 랭킹 string값
		embed = discord.Embed(
			title = "영화순위",
			description = "영화순위입니다.",
			colour= discord.Color.red()
			)
		hdr = {'User-Agent': 'Mozilla/5.0'}
		url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
		print(url)
		req = Request(url, headers=hdr)
		html = urllib.request.urlopen(req)
		bsObj = bs4.BeautifulSoup(html, "html.parser")
		moviechartBase = bsObj.find('div', {'class': 'main_detail'})
		moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
		moviechart2 = moviechart1.find_all('li')

		for i in range(0, 20):
			i1 = i1+1
			stri1 = str(i1) # i1은 영화랭킹을 나타내는데 사용됩니다
			print()
			print(i)
			print()
			moviechartLi1 = moviechart2[i]  # ------------------------- 1등랭킹 영화---------------------------
			moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # 영화박스 나타내는 Div
			moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
			moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # 영화 제목
			print(moviechartLi1MovieName)

			moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
			moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
			moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # 영화 평점
			print(moviechartLi1Ratting)

			moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
			moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # 개봉날짜, 예매율 두개포함한 dd임
			moviechartLi1openDay3 = moviechartLi1openDay2[0]
			moviechartLi1Yerating1 = moviechartLi1openDay2[1]
			moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # 개봉날짜
			print(moviechartLi1openDay)
			moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # 예매율 ,랭킹변동
			print(moviechartLi1Yerating)  # ------------------------- 1등랭킹 영화---------------------------
			print()
			embed.add_field(name='---------------랭킹'+stri1+'위---------------', value='\n영화제목 : '+moviechartLi1MovieName+'\n영화평점 : '+moviechartLi1Ratting+'점'+'\n개봉날짜 : '+moviechartLi1openDay+'\n예매율,랭킹변동 : '+moviechartLi1Yerating, inline=False) # 영화랭킹


		await client.send_message(message.channel, embed=embed)


	if message.content.startswith('!주사위'):
		randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
		print(randomNum)
		if randomNum == 1:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
		if randomNum == 2:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
		if randomNum ==3:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
		if randomNum ==4:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
		if randomNum ==5:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
		if randomNum ==6:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))
			
			
			
			
	if message.content.startswith("!복권"):
		Text = ""
		number = [1, 2, 3, 4, 5, 6, 7]
		count = 0
		for i in range(0, 7):
			num = random.randrange(1, 46)
			number[i] = num
			if count >= 1:
				for i2 in range(0, i):
					if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
						numberText = number[i]
						print("작동 이전값 : " + str(numberText))
						number[i] = random.randrange(1, 46)
						numberText = number[i]
						print("작동 현재값 : " + str(numberText))
						if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
							numberText = number[i]
							print("작동 이전값 : " + str(numberText))
							number[i] = random.randrange(1, 46)
							numberText = number[i]
							print("작동 현재값 : " + str(numberText))
							if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
								numberText = number[i]
								print("작동 이전값 : " + str(numberText))
								number[i] = random.randrange(1, 46)
								numberText = number[i]
								print("작동 현재값 : " + str(numberText))

			count = count + 1
			Text = Text + "  " + str(number[i])
			
		print(Text.strip())
		embed = discord.Embed(
			title="복권 숫자!",
			description=Text.strip(),
			colour=discord.Color.red()
		)
		await client.send_message(message.channel, embed=embed)
		
		
	if message.content.startswith('!사다리'):
		ladder = []
		ladder = message.content[len('!사다리') + 1:].split(" ")
		num_cong = int(ladder[0])
		del (ladder[0])
		if num_cong < len(ladder):
			result_ladder = random.sample(ladder, num_cong)
			result_ladderSTR = ','.join(map(str, result_ladder))
			embed = discord.Embed(
				title="----- 당첨! -----",
				description='```' + result_ladderSTR + '```',
				color=0xff00ff
				)
			await client.send_message(message.channel, embed=embed, tts=False)
		else:
			await client.send_message(message.channel, '```추첨인원이 총 인원과 같거나 많습니다. 재입력 해주세요```', tts=False)

	if message.content.startswith('!타이머'):

		Text = ""
		learn = message.content.split(" ")
		vrsize = len(learn)  # 배열크기
		vrsize = int(vrsize)
		for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
			Text = Text + " " + learn[i]
			
		secint = int(Text)
		sec = secint
		
		for i in range(sec, 0, -1):
			print(i)
			await client.send_message(message.channel, embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
			sleep(1)

		else:
			print("땡")
			await client.send_message(message.channel, embed=discord.Embed(description='타이머 종료'))
			
			

	if message.content.startswith('!사진'):			
		chrome_options = webdriver.ChromeOptions()
		chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# 		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-dev-shm-usage")
		chrome_options.add_argument("--no-sandbox")
# 		options.add_argument('--start-fullscreen')
		chrome_options.headless = True
		driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
		driver.get('https://docs.google.com/spreadsheets/d/1gGOqkMcSau3lXHnP5_UZfEW1rbJOi5czd3w-22QX2j4/pubhtml#')
		# 전체 페이지의 사이즈를 구하여 브라우저의 창 크기를 확대하고 스크린캡처를 합니다.
		page_width = driver.execute_script('return document.body.parentNode.scrollWidth')
		page_height = driver.execute_script('return document.body.parentNode.scrollHeight')
		driver.set_window_size("1050", "2000")
		png = driver.get_screenshot_as_png()

		# 특정 element의 위치를 구하고 selenium 창을 닫습니다.
		element = driver.find_element_by_class_name('waffle')
		image_location = element.location
		image_size = element.size
		driver.quit()

		# 이미지를 element의 위치에 맞춰서 crop 하고 저장합니다.
		im = Image.open(BytesIO(png))
		left = image_location['x']
		top = image_location['y']
		right = image_location['x'] + image_size['width']
		bottom = image_location['y'] + image_size['height']
		im = im.crop((left, top, right, bottom))
		basename = "사진"
		curruntTime = datetime.datetime.now() + datetime.timedelta(hours = 9)
		krnow = curruntTime.strftime('%Y_%m_%d_%H_%M')
		filename = "_".join([basename, krnow])
		im.save("SCREENSHOT", format='PNG')
		pic = os.environ.get("SCREENSHOT")
# 		await message.channel.send(file=discord.File(pic))
		await client.send_message(file=discord.File(pic))

	


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
