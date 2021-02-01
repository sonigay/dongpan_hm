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
	await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name="업무지원", type=1), afk=False)

@client.event
async def on_message(message):
    
			
# 동판채증 문구 안나오는 채널  
	if message.content.startswith('!동판'):
		if message.channel.id != (691736848325672960) and message.channel.id != (688654225286234146) and message.channel.id != (729579799907008544) and message.channel.id != (689426260484423741) and message.channel.id != (689426603184619563) and message.channel.id != (689423874307522589):
			embed = discord.Embed(
			title='',
			description='```fix\n동판정책 채증이 매우 심한관계로\n담당 영업사원 통해서 구두 확인 바랍니다.```',
			color=0xf29886
			)
			await message.channel.send(embed=embed)
		
# 동판 나오는 채널 홍남옥영업2 , 노성수대표님 , 케이플러스 , 케이에스모바일 , 에이치엔씨운정 , MS컴퍼니 	
	if message.content == '!동판':
		if message.channel.id == (691736848325672960) or message.channel.id == (688654225286234146) or message.channel.id == (729579799907008544) or message.channel.id == (689426260484423741) or message.channel.id == (689426603184619563) or message.channel.id == (689423874307522589) or message.channel.id == (689426280738979921):
			gc1 = gspread.authorize(creds1)		
			wks = gc1.open('정책표관리').worksheet('동판구두2')
			result = wks.acell('au2').value #정책 적용일시
			result1 = wks.acell('d6').value # 광기가동판 TV프리미엄 모바일 신규/MNP
			result2 = wks.acell('e6').value # 광기가동판 TV프리미엄 모바일 재가입/정책기변
			result3 = wks.acell('d7').value # 광기가동판 TV베이직 모바일 신규/MNP
			result4 = wks.acell('e7').value # 광기가동판 TV베이직 모바일 재가입/정책기변
			result7 = wks.acell('d9').value # 슬림동판 TV프리미엄 모바일 신규/MNP
			result8 = wks.acell('e9').value # 슬림동판 TV프리미엄 모바일 재가입/정책기변
			result9 = wks.acell('d10').value # 슬림동판 TV베이직 모바일 신규/MNP
			result10 = wks.acell('e10').value # 슬림동판 TV베이직 모바일 재가입/정책기변
			result13 = wks.acell('d12').value # 광랜동판 TV프리미엄 모바일 신규/MNP
			result14 = wks.acell('e12').value # 광랜동판 TV프리미엄 모바일 재가입/정책기변
			result15 = wks.acell('d13').value # 광랜동판 TV베이직 모바일 신규/MNP
			result16 = wks.acell('e13').value # 광랜동판 TV베이직 모바일 재가입/정책기변
			result17 = wks.acell('AD3').value # 상품권추가
			result18 = wks.acell('AI3').value # IOT추가
			result19 = wks.acell('AK3').value # 셋탑추가
			result20 = wks.acell('AM3').value # TV프리2추가
			result21 = wks.acell('AD6').value # 동판 상품권금액
			result22 = wks.acell('AI6').value # 동판 IOT추가
			result23 = wks.acell('AK6').value # 동판 , 후결합 셋탑추가
			result24 = wks.acell('AM6').value # 동판 TV프리2추가
			result25 = wks.acell('AO3').value # 단독 TV프리2 설명
			result26 = wks.acell('AO6').value # 단독 TV프리2 프리미엄
			result27 = wks.acell('AO7').value # 단독 TV프리2 설명
			result28 = wks.acell('AU3').value # 단독 TV프리2 프리미엄
			result29 = wks.acell('AU6').value # 단독 TV프리2 설명
	
			embed = discord.Embed(
				title='🌐 유선 동판 정책',
				description= '```정책 적용 일시내 모바일 개통 및 설치, 결합시 적용```',
				color=0x00ffff
				)
			embed.add_field(
				name="⌛ 정책 적용 일시",
				value='```' + result + '```',
				inline = False
				)
			embed.add_field(
				name="📍 유의사항",
				value='```diff\n-■ 본사 사은품은 3년약정 동판시 지급\n-■ 소호 동판은 개인사업자만 가능(법인 결합 불가)\n-■ (정상요금8회) 미만 요금 납부 후 해지시 수수료 환수\n-■ 해지후 재가입시 수수료 전액 환수\n-  (동일장소 재설치및 가족명의 등)```',
				inline = False
				)
			embed.add_field(
				name= result17,
				value='```' + result21 + '```',
				inline = False
				)
			embed.add_field(
				name= result18,
				value='```' + result22 + '```',
				inline = False
				)
			embed.add_field(
				name= result19,
				value='```' + result23 + '```',
				inline = False
				)
			embed.add_field(
				name= result20,
				value='```' + result24 + '```',
				inline = False
				)
			embed.add_field(
				name= result25,
				value='```' + result26 +"\n"+ result27 + '```',
				inline = False
				)
			embed.add_field(
				name= result28,
				value='```' + result29 + '```',
				inline = False
				)			
			embed1 = discord.Embed(
				title='',
				description= '```-------------💚광기가(1기가)-------------```',
				color=0x83ff30
				)
			embed1.add_field(
				name="TV상품",
				value='```💚TV(17↑)```',
				inline = True
				)
			embed1.add_field(
				name="모바일( 신규/MNP )",
				value='```' + result1 + '```',
				inline = True
				)
			embed1.add_field(
				name="모바일(재가입/기변)",
				value='```' + result2 + '```',
				inline = True
				)
			embed1.add_field(
				name="TV상품",
				value='```💚TV(P)/(B)\n(TV일반요금제제외)```',
				inline = True
				)
			embed1.add_field(
				name="모바일( 신규/MNP )",
				value='```' + result3 + '```',
				inline = True
				)
			embed1.add_field(
				name="모바일(재가입/기변)",
				value='```' + result4 + '```',
				inline = True
				)
			embed2 = discord.Embed(
				title='',
				description= '```-------------💛슬림(500메가)-------------```',
				color=0xf9ff27
				)
			embed2.add_field(
				name="TV상품",
				value='```💛TV(17↑)```',
				inline = True
				)
			embed2.add_field(
				name="모바일( 신규/MNP )",
				value='```' + result7 + '```',
				inline = True
				)
			embed2.add_field(
				name="모바일(재가입/기변)",
				value='```' + result8 + '```',
				inline = True
				)
			embed2.add_field(
				name="TV상품",
				value='```💛TV(P)/(B)\n(TV일반요금제제외)```',
				inline = True
				)
			embed2.add_field(
				name="모바일( 신규/MNP )",
				value='```' + result9 + '```',
				inline = True
				)
			embed2.add_field(
				name="모바일(재가입/기변)",
				value='```' + result10 + '```',
				inline = True
				)
			embed3 = discord.Embed(
				title='',
				description= '```-------------💙광랜(100메가)-------------```',
				color=0x3862ff
				)
			embed3.add_field(
				name="TV상품",
				value='```💙TV(17↑)```',
				inline = True
				)
			embed3.add_field(
				name="모바일( 신규/MNP )",
				value='```' + result13 + '```',
				inline = True
				)
			embed3.add_field(
				name="모바일(재가입/기변)",
				value='```' + result14 + '```',
				inline = True
				)
			embed3.add_field(
				name="TV상품",
				value='```💙TV(P)/(B)\n(TV일반요금제제외)```',
				inline = True
				)
			embed3.add_field(
				name="모바일( 신규/MNP )",
				value='```' + result15 + '```',
				inline = True
				)
			embed3.add_field(
				name="모바일(재가입/기변)",
				value='```' + result16 + '```',
				inline = True
				)

			await message.channel.send(embed=embed)
			await message.channel.send(embed=embed1)
			await message.channel.send(embed=embed2)
			await message.channel.send(embed=embed3)	
		
		
		

	if message.content == '!후결합동판':
		gc1 = gspread.authorize(creds1)		
		wks = gc1.open('정책표관리').worksheet('동판구두2')
		result0 = wks.acell('au1').value #후결합 모바일 적용일시
		result = wks.acell('au2').value #정책 적용일시
		result1 = wks.acell('h6').value # 광기가동판 TV프리미엄 모바일 신규/MNP
		result2 = wks.acell('h19').value # 광기가동판 TV프리미엄 모바일 재가입/정책기변
		result3 = wks.acell('h7').value # 광기가동판 TV베이직 모바일 신규/MNP
		result4 = wks.acell('h20').value # 광기가동판 TV베이직 모바일 재가입/정책기변
		result7 = wks.acell('h9').value # 슬림동판 TV프리미엄 모바일 신규/MNP
		result8 = wks.acell('h22').value # 슬림동판 TV프리미엄 모바일 재가입/정책기변
		result9 = wks.acell('h10').value # 슬림동판 TV베이직 모바일 신규/MNP
		result10 = wks.acell('h23').value # 슬림동판 TV베이직 모바일 재가입/정책기변
		result13 = wks.acell('h12').value # 광랜동판 TV프리미엄 모바일 신규/MNP
		result14 = wks.acell('h25').value # 광랜동판 TV프리미엄 모바일 재가입/정책기변
		result15 = wks.acell('h13').value # 광랜동판 TV베이직 모바일 신규/MNP
		result16 = wks.acell('h26').value # 광랜동판 TV베이직 모바일 재가입/정책기변
		result17 = wks.acell('AD3').value # 상품권추가
		result18 = wks.acell('AI3').value # IOT추가
		result19 = wks.acell('AK3').value # 셋탑추가
		result20 = wks.acell('AM3').value # TV프리2추가
		result21 = wks.acell('AD6').value # 동판 상품권금액
		result22 = wks.acell('AI6').value # 동판 IOT추가
		result23 = wks.acell('AK6').value # 동판 , 후결합 셋탑추가
		result24 = wks.acell('AM6').value # 동판 TV프리2추가
		result25 = wks.acell('AO3').value # 단독 TV프리2 설명
		result26 = wks.acell('AO6').value # 단독 TV프리2 프리미엄
		result27 = wks.acell('AO7').value # 단독 TV프리2 설명

		embed = discord.Embed(
			title='🌐 유선 후결합 동판 정책',
			description= '```정책 적용 일시내 모바일 개통 및 설치, 결합시 적용```',
			color=0x00ffff
			)
		embed.add_field(
			name="⌛ 유선 적용 일시",
			value='```' + result + '```',
			inline = False
			)
		embed.add_field(
			name="⌛ 무선 적용 일시",
			value='```' + result0 + '```',
			inline = False
			)
		embed.add_field(
			name="📍 유의사항",
			value='```diff\n-■ 본사 사은품은 3년약정 동판시 지급\n-■ 소호 동판은 개인사업자만 가능(법인 결합 불가)\n-■ (정상요금8회) 미만 요금 납부 후 해지시 수수료 환수\n-■ 해지후 재가입시 수수료 전액 환수\n-  (동일장소 재설치및 가족명의 등)```',
			inline = False
			)
		embed.add_field(
			name= result17,
			value='```' + result21 + '```',
			inline = False
			)
		embed.add_field(
			name= result18,
			value='```' + result22 + '```',
			inline = False
			)
		embed.add_field(
			name= result19,
			value='```' + result23 + '```',
			inline = False
			)
		embed.add_field(
			name= result20,
			value='```' + result24 + '```',
			inline = False
			)
		embed.add_field(
			name= result25,
			value='```' + result26 +"\n"+ result27 + '```',
			inline = False
			)
		embed1 = discord.Embed(
			title='',
			description= '```-------------💚광기가(1기가)-------------```',
			color=0x83ff30
			)
		embed1.add_field(
			name="TV상품",
			value='```💚TV(17↑)```',
			inline = True
			)
		embed1.add_field(
			name="모바일( 신규/MNP )",
			value='```' + result1 + '```',
			inline = True
			)
		embed1.add_field(
			name="모바일(재가입/기변)",
			value='```' + result2 + '```',
			inline = True
			)
		embed1.add_field(
			name="TV상품",
			value='```💚TV(P)/(B)\n(TV일반요금제제외)```',
			inline = True
			)
		embed1.add_field(
			name="모바일( 신규/MNP )",
			value='```' + result3 + '```',
			inline = True
			)
		embed1.add_field(
			name="모바일(재가입/기변)",
			value='```' + result4 + '```',
			inline = True
			)
		embed2 = discord.Embed(
			title='',
			description= '```-------------💛슬림(500메가)-------------```',
			color=0xf9ff27
			)
		embed2.add_field(
			name="TV상품",
			value='```💛TV(17↑)```',
			inline = True
			)
		embed2.add_field(
			name="모바일( 신규/MNP )",
			value='```' + result7 + '```',
			inline = True
			)
		embed2.add_field(
			name="모바일(재가입/기변)",
			value='```' + result8 + '```',
			inline = True
			)
		embed2.add_field(
			name="TV상품",
			value='```💛TV(P)/(B)\n(TV일반요금제제외)```',
			inline = True
			)
		embed2.add_field(
			name="모바일( 신규/MNP )",
			value='```' + result9 + '```',
			inline = True
			)
		embed2.add_field(
			name="모바일(재가입/기변)",
			value='```' + result10 + '```',
			inline = True
			)
		embed3 = discord.Embed(
			title='',
			description= '```-------------💙광랜(100메가)-------------```',
			color=0x3862ff
			)
		embed3.add_field(
			name="TV상품",
			value='```💙TV(17↑)```',
			inline = True
			)
		embed3.add_field(
			name="모바일( 신규/MNP )",
			value='```' + result13 + '```',
			inline = True
			)
		embed3.add_field(
			name="모바일(재가입/기변)",
			value='```' + result14 + '```',
			inline = True
			)
		embed3.add_field(
			name="TV상품",
			value='```💙TV(P)/(B)\n(TV일반요금제제외)```',
			inline = True
			)
		embed3.add_field(
			name="모바일( 신규/MNP )",
			value='```' + result15 + '```',
			inline = True
			)
		embed3.add_field(
			name="모바일(재가입/기변)",
			value='```' + result16 + '```',
			inline = True
			)
		await message.channel.send(embed=embed)
		await message.channel.send(embed=embed1)
		await message.channel.send(embed=embed2)
		await message.channel.send(embed=embed3)

		
		
		
		
	if message.content.startswith('!공짜폰'):
		SearchID = message.content[len('!공짜폰')+1:]
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('정책표관리').worksheet('HM상권무선공짜출력')
		wks1 = gc1.open('정책표관리').worksheet('HM무선공짜출력')
		wks.update_acell('A1', SearchID)
		wks1.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		result1 = wks1.acell('B1').value
		
		embed1 = discord.Embed(
			title = ' 오늘의 ' + SearchID + ' 공짜폰 안내 ',
			description= '**```css\n할부원금 0원 공시 현금개통시\n' +SearchID+ ' 공짜폰 마진 ```**',
			color=0x4BAF4B
			)
		embed1.add_field(
			name="상권 점프개통시",
			value= '**```css\n' + result + ' ```**',
			inline=True
			)
		embed1.add_field(
			name="자체 P코드 개통시",
			value= '**```css\n' + result1 + ' ```**',
			inline=True
			)
		embed1.add_field(
			name="⭐ 주의사항",
			value= '**```css\n혹시라도 계산이 정확하지 않을수 있으니\n참고만 해주세요.```**',
			inline=False
			)		
		embed2 = discord.Embed(
			title = SearchID + ' 공짜폰 조회!! ',
			description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + '```',
			color=0x4BAF4B
			)
		await client.get_channel(674652501693300737).send(embed=embed2)
		await message.channel.send(embed=embed1)
		
		
		
		
	if message.content.startswith('!외국인공짜폰'):
		SearchID = message.content[len('!외국인공짜폰')+1:]
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('정책표관리').worksheet('HM외국인공짜출력')
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
		await client.get_channel(674654114592063498).send(embed=embed2)
		await message.channel.send(embed=embed1)
		
		
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
		await client.get_channel(672022974223876096).send(embed=embed2)
		await message.channel.send(embed=embed1)


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
		await message.channel.send(embed=embed1)
		await client.get_channel(667343258296254464).send(embed=embed2)
		
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
		await message.channel.send(member, embed=embed)
		

	if message.content.startswith('!전달'):
		if message.author.id == (315237238940106754) or message.author.id == (329988391812726784) :
			embed = discord.Embed(    
				title = "📌 공지사항",
				description= '```' + message.content[4:] + '```',
				color=0xFF0000	
				)
			await client.get_channel(688654225286234146).send(embed=embed)
			await client.get_channel(689423774021320864).send(embed=embed)
			await client.get_channel(689423821668745221).send(embed=embed)
			await client.get_channel(689423849418260528).send(embed=embed)
			await client.get_channel(689423874307522589).send(embed=embed)
			await client.get_channel(689423911049625650).send(embed=embed)
			await client.get_channel(689423931907768365).send(embed=embed)
			await client.get_channel(689423951646294016).send(embed=embed)
			await client.get_channel(689423972596580498).send(embed=embed)
			await client.get_channel(689424003831431188).send(embed=embed)
			await client.get_channel(689424036316315668).send(embed=embed)
			await client.get_channel(689424058286080025).send(embed=embed)
			await client.get_channel(689424077420757001).send(embed=embed)
			await client.get_channel(689424098467905567).send(embed=embed)
			await client.get_channel(689424129040056324).send(embed=embed)
			await client.get_channel(689424150447915023).send(embed=embed)
			await client.get_channel(689424171666505752).send(embed=embed)
			await client.get_channel(689424193237942299).send(embed=embed)
			await client.get_channel(689424220643393582).send(embed=embed)
			await client.get_channel(689424319482298449).send(embed=embed)
			await client.get_channel(689425993739665516).send(embed=embed)
			await client.get_channel(689426019433578551).send(embed=embed)
			await client.get_channel(689426047946588262).send(embed=embed)
			await client.get_channel(689426068511391747).send(embed=embed)
			await client.get_channel(689426089466265600).send(embed=embed)
			await client.get_channel(689426156424134693).send(embed=embed)
			await client.get_channel(689426210601959475).send(embed=embed)
			await client.get_channel(689426260484423741).send(embed=embed)
			await client.get_channel(689426280738979921).send(embed=embed)
			await client.get_channel(689426304113704967).send(embed=embed)
			await client.get_channel(689426342147522630).send(embed=embed)
			await client.get_channel(689426427040497677).send(embed=embed)
			await client.get_channel(689426448532111383).send(embed=embed)
			await client.get_channel(689426471172702258).send(embed=embed)
			await client.get_channel(689426490974011431).send(embed=embed)
			await client.get_channel(689426517360509002).send(embed=embed)
			await client.get_channel(689426547920339016).send(embed=embed)
			await client.get_channel(689426570955325450).send(embed=embed)
			await client.get_channel(689426603184619563).send(embed=embed)
			await client.get_channel(689426625892319261).send(embed=embed)
			await client.get_channel(689426647732060226).send(embed=embed)
			await client.get_channel(689426671144796170).send(embed=embed)
			await client.get_channel(689426704443244580).send(embed=embed)
			await client.get_channel(689426726123601960).send(embed=embed)
			await client.get_channel(689426807443030016).send(embed=embed)
			await client.get_channel(689426834055626770).send(embed=embed)
			await client.get_channel(689426854498926623).send(embed=embed)
			await client.get_channel(689426874904084532).send(embed=embed)
			await client.get_channel(689426896282189836).send(embed=embed)
			await client.get_channel(689426919204061190).send(embed=embed)
			await client.get_channel(689426964389691496).send(embed=embed)
			await client.get_channel(689427031716528146).send(embed=embed)
			await client.get_channel(689427058014814218).send(embed=embed)
			await client.get_channel(689427081247064129).send(embed=embed)
			await client.get_channel(689427103136874536).send(embed=embed)
			await client.get_channel(689427138377678888).send(embed=embed)
			await client.get_channel(689427162302119961).send(embed=embed)
			await client.get_channel(689427184443588632).send(embed=embed)
			await client.get_channel(689427209018015842).send(embed=embed)
			await client.get_channel(689427243008655360).send(embed=embed)
			await client.get_channel(689427387859206168).send(embed=embed)
			await client.get_channel(689427632181477471).send(embed=embed)
			await client.get_channel(689501698535718927).send(embed=embed)
			await client.get_channel(689501731398221953).send(embed=embed)
			await client.get_channel(689501760276267066).send(embed=embed)
			await client.get_channel(689501793830436968).send(embed=embed)
			await client.get_channel(689501820430975049).send(embed=embed)
			await client.get_channel(689501843516424304).send(embed=embed)
			await client.get_channel(689501888193757229).send(embed=embed)
			await client.get_channel(689501922952216585).send(embed=embed)
			await client.get_channel(689501951884263601).send(embed=embed)
			await client.get_channel(689501972801650848).send(embed=embed)
			await client.get_channel(689501996348473384).send(embed=embed)
			await client.get_channel(689502016002981970).send(embed=embed)
			await client.get_channel(689502037905637410).send(embed=embed)
			await client.get_channel(689502305296318472).send(embed=embed)
			await client.get_channel(689502362628522014).send(embed=embed)
			await client.get_channel(689502386250842164).send(embed=embed)
			await client.get_channel(689502415518564357).send(embed=embed)
			await client.get_channel(689502463434293352).send(embed=embed)
			await client.get_channel(689502486117220404).send(embed=embed)
			await client.get_channel(689502509873758306).send(embed=embed)
			await client.get_channel(689502531851649024).send(embed=embed)
			await client.get_channel(689502551967662090).send(embed=embed)
			await client.get_channel(689502574122106924).send(embed=embed)
			await client.get_channel(689502594871066678).send(embed=embed)
			
			
		
	if message.content == '!명령어':
		command_list = ''
		command_list += '!명령어\n'     #!명령어
		command_list += '!모델명\n'     #!모델명
		command_list += '!신규안내\n'     #!신규안내
		command_list += '!정산\n'     #!정산		
		
		embed = discord.Embed(
			title = ":keyboard: 기본명령어",
			description= '```fix\n' + command_list + '```',
			color=0xFFD5B4
			)
		embed.add_field(
			name="📶 정책관련 명령어 ",
			value= '```diff\n- !정책표\n- !끝단가\n---< 상권정책 점프개통 구두포함 끝단가 출력. >\n- !원정책끝단가\n---< 자체 P코드 직접 개통 및 원정책 끝단가출력. >\n- !외국인끝단가\n---< 외국인 정책 끝단가 출력. >\n- !비하인드\n---< 비하인드 명령어는 음성지원만 확인가능합니다. >\n- !디메릿\n---< 현재 디메릿 적용중인 지역 확인 >\n+ !디메릿 [지역명]\n---< ex)!디메릿 강서구 >\n+ !단가 모델명 요금제군 유형\n---< ex)!단가 N976 A군 MNP >\n+ !외국인단가 모델명 요금제군 유형\n---< ex)!외국인단가 N976 A군 MNP >\n+ !공짜폰 요금제군 유형\n---< ex)!공짜폰 C군 MNP >\n+ !외국인공짜폰 요금제군 유형\n---< ex)!외국인공짜폰 A군 신규 > ```',
			inline = False
			)
		embed.add_field(
			name="📲 재고관련 명령어 ",
			value= '```diff\n- !주문\n---< ex)!주문 N976 화이트 1대 보내주세요 >\n+ !재고 모델명\n---< ex)!재고 N976 >\n+ !재고 [구단위]\n---< ex)!재고 남동구 >\n+ !퀵비 [동단위/동단위]\n---< ex)!퀵비 논현동/가좌동 > ```',
			inline = False
			)
		embed.add_field(
			name="🌐 동판관련 명령어 ",
			value= '```Cs\n# !결합\n\n# !동판\n\n# !후결합동판\n\n# !인터넷요금\n\n\n\n ```',
			inline = True
			)
		embed.add_field(
			name="🎲 기타 명령어 ",
			value= '```diff\n= !영화순위\n= !주사위\n= !복권\n+ !나이 생년-월-일 \n---< ex)!나이 2002-02-01 >\n+ !유지기간 개통일\n---< ex)!유지기간 2020-01-01 >\n+ !사다리 뽑을인원수 인원1 인원2 인원3...\n---< ex)!사다리 2 홍길동 갑돌이 갑순이 >\n+ !타이머 초시간\n---< ex)!타이머 5 >```',
			inline = True
			)
		await message.channel.send(embed=embed)
        
	if message.content == '!영업명령어':
		command_list = ''
		command_list += '!영업명령어\n'     #!명령어        
		command_list += '!모델명\n'     #!모델명
		command_list += '!거래처\n'     #!모델명
		command_list += '!플러스관계설정\n'     #!플러스관계설정
		command_list += '!에이스관계설정\n'     #!에이스관계설정
		command_list += '!신규안내\n'     #!신규안내
		command_list += '!정산\n'     #!정산
		
		embed = discord.Embed(
			title = "🚗 영업부 기본명령어",
			description= '```fix\n' + command_list + '```',
			color=0xFFD5B4
			)
		embed.add_field(
			name="📈 실적관련 명령어 ",
			value= '```diff\n- !전월실적\n---< 전월 전체실적 >\n+ !전월실적 영업사원이름\n---< ex)!전월실적 홍길동 >\n- !당월실적\n---< 데이터 입력일까지 당월 전체실적 >\n+ !당월실적 영업사원이름\n---< ex)!당월실적 홍길동 > ```',
			inline = False
			)
		embed.add_field(
			name="📶 정책관련 명령어 ",
			value= '```diff\n- !정책표\n- !끝단가\n---< 상권정책 점프개통 구두포함 끝단가 출력. >\n- !원정책끝단가\n---< 자체 P코드 직접 개통 및 원정책 끝단가출력. >\n- !외국인끝단가\n---< 외국인 정책 끝단가 출력. >\n- !비하인드\n---< 비하인드 명령어는 음성지원만 확인가능합니다. >\n- !디메릿\n---< 현재 디메릿 적용중인 지역 확인 >\n+ !디메릿 [지역명]\n---< ex)!디메릿 강서구 >\n+ !단가 모델명 요금제군 유형\n---< ex)!단가 N976 A군 MNP >\n+ !외국인단가 모델명 요금제군 유형\n---< ex)!외국인단가 N976 A군 MNP >\n+ !공짜폰 요금제군 유형\n---< ex)!공짜폰 C군 MNP >\n+ !외국인공짜폰 요금제군 유형\n---< ex)!외국인공짜폰 A군 신규 > ```',
			inline = False
			)
		embed.add_field(
			name="📲 재고관련 명령어 ",
			value= '```diff\n- !주문\n---< ex)!주문 A305 A505 배정부탁드립니다. >\n+ !재고 모델명\n---< ex)!재고 N976 >\n+ !재고 거래처코드\n---< ex)!재고 A34 >\n- !불량\n---< 전체불량현황 >\n+ !불량 거래처코드\n---< ex)!불량 A34 >\n- !유심\n---< 10개 미만 유심현황 >\n+ !유심 전체\n---< 거래처 총 유심현황 >\n+ !퀵비 [동단위/동단위]\n---< ex)!퀵비 논현동/가좌동 >\n\n퀵비 멍령어는 실행은 되지만\n데이터량이 많아 다소 결과가 늦게 나옴 ```',
			inline = False
			)
		embed.add_field(
			name="🌐 동판관련 명령어 ",
			value= '```Cs\n# !결합\n\n# !동판\n\n# !후결합동판\n\n# !인터넷요금\n\n\n\n ```',
			inline = True
			)
		embed.add_field(
			name="🎲 기타 명령어 ",
			value= '```diff\n= !영화순위\n= !주사위\n= !복권\n+ !나이 생년-월-일 \n---< ex)!나이 2002-02-01 >\n+ !유지기간 개통일\n---< ex)!유지기간 2020-01-01 >\n+ !사다리 뽑을인원수 인원1 인원2 인원3...\n---< ex)!사다리 2 홍길동 갑돌이 갑순이 >\n+ !타이머 초시간\n---< ex)!타이머 5 >```',
			inline = True
			)
		await message.channel.send(embed=embed)	
		
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
		await message.channel.send(embed=embed)
		
		
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
		await message.channel.send(embed=embed)	
		
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


		await message.channel.send(embed=embed)


	if message.content.startswith('!주사위'):
		randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
		print(randomNum)
		if randomNum == 1:
			await message.channel.send(embed=discord.Embed(description=':game_die: '+ ':one:'))
		if randomNum == 2:
			await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':two:'))
		if randomNum ==3:
			await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':three:'))
		if randomNum ==4:
			await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':four:'))
		if randomNum ==5:
			await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':five:'))
		if randomNum ==6:
			await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':six: '))
			
			
			
			
	if message.content.startswith("!복권"):
		Text = ""
		number = [1, 2, 3, 4, 5, 6]
		count = 0
		for i in range(0, 6):
			num = random.randrange(1, 45)
			number[i] = num
			if count >= 1:
				for i2 in range(0, i):
					if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
						numberText = number[i]
						print("작동 이전값 : " + str(numberText))
						number[i] = random.randrange(1, 45)
						numberText = number[i]
						print("작동 현재값 : " + str(numberText))
						if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
							numberText = number[i]
							print("작동 이전값 : " + str(numberText))
							number[i] = random.randrange(1, 45)
							numberText = number[i]
							print("작동 현재값 : " + str(numberText))
							if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
								numberText = number[i]
								print("작동 이전값 : " + str(numberText))
								number[i] = random.randrange(1, 45)
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
		await message.channel.send(embed=embed)
		
		
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
			await message.channel.send(embed=embed, tts=False)
		else:
			await message.channel.send('```추첨인원이 총 인원과 같거나 많습니다. 재입력 해주세요```', tts=False)

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
			await message.channel.send(embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
			sleep(1)

		else:
			print("땡")
			await message.channel.send(embed=discord.Embed(description='타이머 종료'))

	


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
