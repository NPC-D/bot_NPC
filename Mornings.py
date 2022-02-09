import datetime
import requests
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from io import BytesIO
import json
import time
import os
from random import choice

def Morning(qqnum,id,times,luck):
    q_ = json.load(open("./config.json", encoding='utf-8')) # 刷新数据

    # -------------------打开图片创建画板--------------------------
    # 随机选取图片
    path_ =  "./mornings"
    path_list = os.listdir(path_ )
    path_random = choice(path_list)
    image_path = path_+'\\'+path_random
    
    bg = Image.open(image_path)
    draw = ImageDraw.Draw(bg)
    # ------------------------------------------------------------

    # 头像模块----------------------------------------------------
    x, y = 55,251
    box = (x,y, x+100, y+100)
    # 请求头像
    q = requests.get("http://q1.qlogo.cn/g?b=qq&nk="+id+"&s=3" )
    image = Image.open(BytesIO(q.content))
    # 头像和圆形蒙版
    mask = Image.new('RGBA', (100, 100), color=(0,0,0,0)) # 创建一个蒙版
    mask_draw = ImageDraw.Draw(mask) # 在这个蒙板上画的
    mask_draw.ellipse((0,0, 100,100), fill=(0,0,0,255))
    bg.paste(image, box, mask)
    # 头像装饰
    am = Image.open('./decorate/s2.png').convert('RGBA')
    am = am.resize((135,135),Image.ANTIALIAS)
    bg.paste(am, (x-18, y-18),am)
    # -------------------------------------------------------------
    
    # 问候语--------------------------------------------------------
    x = 45
    y = 83
    text = "Morning"
    size = 35
    color = (255,255,255)
    font = './ttf/脚印星星字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)  
    # 昵称
    x,y = (45,y-59) 
    text = qqnum  
    color = (255,255,255)           
    size = 52 
    font = './ttf/脚印星星字体.ttf'                                        
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    # ---------------------------------------------------------------
   
    # 累计天数-------------------------------------------------------
    x,y = (392,160)
    text = str(q_[id]["Sign_in"])
    size = 40        
    color = (211,64,33)
    font = './ttf/腾祥爱情体简字体.ttf'                            
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    (xx,yy) = font.getsize(text)
    # 固定值day
    y = 180
    text = "days"
    size = 23       
    color = (0,0,0)            
    font = './ttf/脚印星星字体.ttf'                    
    font = ImageFont.truetype(font,size)
    draw.text((x+8+xx,y),text,color,font = font)
    # ---------------------------------------------------------------

    # 当前好感度
    x,y = (358,221)
    text = str(q_[id]["Favorability"]/100)                
    color = (0,0,0)           
    size = 32                      
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # --------------------------------------------------------------------------
    text_qqi = ["路人","陌生","初识","熟悉","亲近","信赖","爱慕","喜欢","热恋"]
    text_t = ["排斥","警惕","闲聊","在意","想念","唠叨","思念","关注","陪伴"]
    if q_[id]["Favorability"] <=1000:
        text0 =str('0 '+'['+text_qqi[0]+']')
        x0 = int((q_[id]["Favorability"]/1000)*222)
        text1 = text_t[0]
        num = str((1000-q_[id]["Favorability"])/100)
    elif 1000 < q_[id]["Favorability"] <=2500:
        text0 =str('1 '+'['+text_qqi[1]+']')
        x0 = int((q_[id]["Favorability"]/2500)*222)
        text1 = text_t[1]
        num = str((2500-q_[id]["Favorability"])/100)
    elif 2500 < q_[id]["Favorability"] <=5000:
        text0 =str('2 '+'['+text_qqi[2]+']')
        x0 = int((q_[id]["Favorability"]/5000)*222)
        text1 = text_t[2]
        num = str((5000-q_[id]["Favorability"])/100)
    elif 5000 < q_[id]["Favorability"] <=10000:
        text0 =str('3 '+'['+text_qqi[3]+']')
        x0 = int((q_[id]["Favorability"]/10000)*222)
        text1 = text_t[3]
        num = str((10000-q_[id]["Favorability"])/100)
    elif 10000 < q_[id]["Favorability"] <=20000:
        text0 =str('4 '+'['+text_qqi[4]+']')
        x0 = int((q_[id]["Favorability"]/20000)*222)
        text1 = text_t[4]
        num = str((20000-q_[id]["Favorability"])/100)
    elif 20000 < q_[id]["Favorability"] <=30000:
        text0 =str('5 '+'['+text_qqi[5]+']')
        x0 = int((q_[id]["Favorability"]/30000)*222)
        text1 = text_t[5]
        num = str((30000-q_[id]["Favorability"])/100)
    elif 30000 < q_[id]["Favorability"] <=50000:
        text0 =str('6 '+'['+text_qqi[6]+']')
        x0 = int((q_[id]["Favorability"]/50000)*222)
        text1 = text_t[6]
        num = str((50000-q_[id]["Favorability"])/100)        

    # 进度条整体长222 加载覆盖渐变进度条 x0是进度条的数值表现
    img = Image.open('./Gradualchange/Almost.png')
    width, height = img.size
    x = 100
    img_ANTIALIAS = img.resize((x, int(x*height/width)), Image.ANTIALIAS)  # ANTIALIAS 高质量下采样滤波
    box = (0,0, x0, 21)
    region = img_ANTIALIAS.crop(box)
    bg.paste(region,(223,272),region)
    # 好感度
    x,y = (223+108,305) 
    color = (0,0,0)           
    size = 16                     
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text0,color,font = font) 
    # 态度
    x,y = (223+138,324)
    color = (0,0,0)           
    size = 16                     
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text1,color,font = font)
    # 好感度差值
    x,y = (223+115,342)
    text = num+"  好感度"       
    color = (0,0,0)           
    size = 16               
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    # ----------------------------------------------------------------------   
    # 时间
    time_local = time.localtime(times)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    x,y = (275,375)
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),str(dt),color,font = font)   
    # 金币
    x,y = (622,266)
    text = str(luck*(int(luck/2))+luck)     
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    if luck > 7:
        text0 = "两倍幸运值！"     
        text = str(2*((8+luck*(int(luck/2)))/100))    
    elif luck > 10:
        text0 = "三倍幸运值！"     
        text = str(3*((8+luck*(int(luck/2)))/100)) 
    else:
        text0 = "额外金币+" + str(luck)
        text = str(((6+luck*(int(luck/2)))/100))     

    # 额外区域        
    x2,y2 = (600,340)
    color = (0,0,0)           
    size = 27                  
    font = './ttf/腾祥爱情体简字体.ttf'
    font = ImageFont.truetype(font,size)
    draw.text((x2,y2),text0,color,font = font)
    # 好感度++
    x,y = (641,240)
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    bg.save('ph.png')

def noon(qqnum,id,times,luck):
    q_ = json.load(open("./config.json", encoding='utf-8')) # 刷新数据

    # -------------------打开图片创建画板--------------------------
    # 随机选取图片
    path_ =  "./noons"
    path_list = os.listdir(path_ )
    path_random = choice(path_list)
    image_path = path_+'\\'+path_random
    
    bg = Image.open(image_path)
    draw = ImageDraw.Draw(bg)
    # ------------------------------------------------------------

    # 头像模块----------------------------------------------------
    x, y = 55,251
    box = (x,y, x+100, y+100)
    # 请求头像
    q = requests.get("http://q1.qlogo.cn/g?b=qq&nk="+id+"&s=3" )
    image = Image.open(BytesIO(q.content))
    # 头像和圆形蒙版
    mask = Image.new('RGBA', (100, 100), color=(0,0,0,0)) # 创建一个蒙版
    mask_draw = ImageDraw.Draw(mask) # 在这个蒙板上画的
    mask_draw.ellipse((0,0, 100,100), fill=(0,0,0,255))
    bg.paste(image, box, mask)
    # 头像装饰
    am = Image.open('./decorate/s1.png').convert('RGBA')
    am = am.resize((135,135),Image.ANTIALIAS)
    bg.paste(am, (x-11, y-14),am)
    # -------------------------------------------------------------
    
    # 问候语--------------------------------------------------------
    x = 45
    y = 83
    text = "Afternoon"
    size = 35
    color = (0,0,0)
    font = './ttf/青鸟华光简魏体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)  
    # 昵称
    x,y = (45,y-59) 
    text = qqnum  
    color = (0,0,0)           
    size = 52 
    font = './ttf/青鸟华光简魏体字体.ttf'                                        
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    # ---------------------------------------------------------------
   
    # 累计天数-------------------------------------------------------
    x,y = (386,165)
    text = str(q_[id]["Sign_in"])
    size = 40        
    color = (211,64,33)
    font = './ttf/腾祥爱情体简字体.ttf'                            
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    (xx,yy) = font.getsize(text)
    # 固定值day
    y = 180
    text = "days"
    size = 30       
    color = (0,0,0)            
    font = './ttf/青鸟华光简魏体字体.ttf'                    
    font = ImageFont.truetype(font,size)
    draw.text((x+8+xx,y),text,color,font = font)
    # ---------------------------------------------------------------

    # 当前好感度
    x,y = (358,221)
    text = str(q_[id]["Favorability"]/100)                
    color = (0,0,0)           
    size = 32                      
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # --------------------------------------------------------------------------
    text_qqi = ["路人","陌生","初识","熟悉","亲近","信赖","爱慕","喜欢","热恋"]
    text_t = ["排斥","警惕","闲聊","在意","想念","唠叨","思念","关注","陪伴"]
    if q_[id]["Favorability"] <=1000:
        text0 =str('0 '+'['+text_qqi[0]+']')
        x0 = int((q_[id]["Favorability"]/1000)*222)
        text1 = text_t[0]
        num = str((1000-q_[id]["Favorability"])/100)
    elif 1000 < q_[id]["Favorability"] <=2500:
        text0 =str('1 '+'['+text_qqi[1]+']')
        x0 = int((q_[id]["Favorability"]/2500)*222)
        text1 = text_t[1]
        num = str((2500-q_[id]["Favorability"])/100)
    elif 2500 < q_[id]["Favorability"] <=5000:
        text0 =str('2 '+'['+text_qqi[2]+']')
        x0 = int((q_[id]["Favorability"]/5000)*222)
        text1 = text_t[2]
        num = str((5000-q_[id]["Favorability"])/100)
    elif 5000 < q_[id]["Favorability"] <=10000:
        text0 =str('3 '+'['+text_qqi[3]+']')
        x0 = int((q_[id]["Favorability"]/10000)*222)
        text1 = text_t[3]
        num = str((10000-q_[id]["Favorability"])/100)
    elif 10000 < q_[id]["Favorability"] <=20000:
        text0 =str('4 '+'['+text_qqi[4]+']')
        x0 = int((q_[id]["Favorability"]/20000)*222)
        text1 = text_t[4]
        num = str((20000-q_[id]["Favorability"])/100)
    elif 20000 < q_[id]["Favorability"] <=30000:
        text0 =str('5 '+'['+text_qqi[5]+']')
        x0 = int((q_[id]["Favorability"]/30000)*222)
        text1 = text_t[5]
        num = str((30000-q_[id]["Favorability"])/100)
    elif 30000 < q_[id]["Favorability"] <=50000:
        text0 =str('6 '+'['+text_qqi[6]+']')
        x0 = int((q_[id]["Favorability"]/50000)*222)
        text1 = text_t[6]
        num = str((50000-q_[id]["Favorability"])/100)        

    # 进度条整体长222 加载覆盖渐变进度条 x0是进度条的数值表现
    img = Image.open('./Gradualchange/Flare.png')
    width, height = img.size
    x = 100
    img_ANTIALIAS = img.resize((x, int(x*height/width)), Image.ANTIALIAS)  # ANTIALIAS 高质量下采样滤波
    box = (0,0, x0, 21)
    region = img_ANTIALIAS.crop(box)
    bg.paste(region,(223,272),region)
    # 好感度
    x,y = (223+108,305) 
    color = (0,0,0)           
    size = 16                     
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text0,color,font = font) 
    # 态度
    x,y = (223+138,324)
    color = (0,0,0)           
    size = 16                     
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text1,color,font = font)
    # 好感度差值
    x,y = (223+115,342)
    text = num+"  好感度"       
    color = (0,0,0)           
    size = 16               
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    # ----------------------------------------------------------------------   
    # 时间
    time_local = time.localtime(times)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    x,y = (275,375)
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),str(dt),color,font = font)   
    # 金币
    x,y = (622,266)
    text = str(luck*(int(luck/2))+luck)     
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    if luck > 7:
        text0 = "两倍幸运值！"     
        text = str(2*((8+luck*(int(luck/2)))/100))    
    elif luck > 10:
        text0 = "三倍幸运值！"     
        text = str(3*((8+luck*(int(luck/2)))/100)) 
    else:
        text0 = "额外金币+" + str(luck)
        text = str(((6+luck*(int(luck/2)))/100))     

    # 额外区域        
    x2,y2 = (600,338)
    color = (0,0,0)           
    size = 27                  
    font = './ttf/腾祥爱情体简字体.ttf'
    font = ImageFont.truetype(font,size)
    draw.text((x2,y2),text0,color,font = font)
    # 好感度++
    x,y = (641,240)
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    bg.save('ph.png')

def Afternoons(qqnum,id,times,luck):
    q_ = json.load(open("./config.json", encoding='utf-8')) # 刷新数据

    # -------------------打开图片创建画板--------------------------
    # 随机选取图片
    path_ =  "./afternoons"
    path_list = os.listdir(path_ )
    path_random = choice(path_list)
    image_path = path_+'\\'+path_random
    
    bg = Image.open(image_path)
    draw = ImageDraw.Draw(bg)
    # ------------------------------------------------------------

    # 头像模块----------------------------------------------------
    x, y = 55,251
    box = (x,y, x+100, y+100)
    # 请求头像
    q = requests.get("http://q1.qlogo.cn/g?b=qq&nk="+id+"&s=3" )
    image = Image.open(BytesIO(q.content))
    # 头像和圆形蒙版
    mask = Image.new('RGBA', (100, 100), color=(0,0,0,0)) # 创建一个蒙版
    mask_draw = ImageDraw.Draw(mask) # 在这个蒙板上画的
    mask_draw.ellipse((0,0, 100,100), fill=(0,0,0,255))
    bg.paste(image, box, mask)
    # 头像装饰
    am = Image.open('./decorate/s3.png').convert('RGBA')
    am = am.resize((135,135),Image.ANTIALIAS)
    bg.paste(am, (x-14, y-15),am)
    # -------------------------------------------------------------
    
    # 问候语--------------------------------------------------------
    x = 45
    y = 83
    text = "Afternoon"
    size = 35
    color = (204,204,204)
    font = './ttf/青鸟华光简魏体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)  
    # 昵称
    x,y = (45,y-59) 
    text = qqnum  
    color = (204,204,204)         
    size = 52 
    font = './ttf/青鸟华光简魏体字体.ttf'                                        
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    # ---------------------------------------------------------------
   
    # 累计天数-------------------------------------------------------
    x,y = (386,165)
    text = str(q_[id]["Sign_in"])
    size = 40        
    color = (211,64,33)
    font = './ttf/腾祥爱情体简字体.ttf'                            
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    (xx,yy) = font.getsize(text)
    # 固定值day
    y = 180
    text = "days"
    size = 30       
    color = (0,0,0)            
    font = './ttf/青鸟华光简魏体字体.ttf'                    
    font = ImageFont.truetype(font,size)
    draw.text((x+8+xx,y),text,color,font = font)
    # ---------------------------------------------------------------

    # 当前好感度
    x,y = (358,221)
    text = str(q_[id]["Favorability"]/100)                
    color = (0,0,0)           
    size = 32                      
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # --------------------------------------------------------------------------
    text_qqi = ["路人","陌生","初识","熟悉","亲近","信赖","爱慕","喜欢","热恋"]
    text_t = ["排斥","警惕","闲聊","在意","想念","唠叨","思念","关注","陪伴"]
    if q_[id]["Favorability"] <=1000:
        text0 =str('0 '+'['+text_qqi[0]+']')
        x0 = int((q_[id]["Favorability"]/1000)*222)
        text1 = text_t[0]
        num = str((1000-q_[id]["Favorability"])/100)
    elif 1000 < q_[id]["Favorability"] <=2500:
        text0 =str('1 '+'['+text_qqi[1]+']')
        x0 = int((q_[id]["Favorability"]/2500)*222)
        text1 = text_t[1]
        num = str((2500-q_[id]["Favorability"])/100)
    elif 2500 < q_[id]["Favorability"] <=5000:
        text0 =str('2 '+'['+text_qqi[2]+']')
        x0 = int((q_[id]["Favorability"]/5000)*222)
        text1 = text_t[2]
        num = str((5000-q_[id]["Favorability"])/100)
    elif 5000 < q_[id]["Favorability"] <=10000:
        text0 =str('3 '+'['+text_qqi[3]+']')
        x0 = int((q_[id]["Favorability"]/10000)*222)
        text1 = text_t[3]
        num = str((10000-q_[id]["Favorability"])/100)
    elif 10000 < q_[id]["Favorability"] <=20000:
        text0 =str('4 '+'['+text_qqi[4]+']')
        x0 = int((q_[id]["Favorability"]/20000)*222)
        text1 = text_t[4]
        num = str((20000-q_[id]["Favorability"])/100)
    elif 20000 < q_[id]["Favorability"] <=30000:
        text0 =str('5 '+'['+text_qqi[5]+']')
        x0 = int((q_[id]["Favorability"]/30000)*222)
        text1 = text_t[5]
        num = str((30000-q_[id]["Favorability"])/100)
    elif 30000 < q_[id]["Favorability"] <=50000:
        text0 =str('6 '+'['+text_qqi[6]+']')
        x0 = int((q_[id]["Favorability"]/50000)*222)
        text1 = text_t[6]
        num = str((50000-q_[id]["Favorability"])/100)        

    # 进度条整体长222 加载覆盖渐变进度条 x0是进度条的数值表现
    img = Image.open('./Gradualchange/Piglet.png')
    width, height = img.size
    x = 100
    img_ANTIALIAS = img.resize((x, int(x*height/width)), Image.ANTIALIAS)  # ANTIALIAS 高质量下采样滤波
    box = (0,0, x0, 21)
    region = img_ANTIALIAS.crop(box)
    bg.paste(region,(223,272),region)
    # 好感度
    x,y = (223+108,305) 
    color = (0,0,0)           
    size = 16                     
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text0,color,font = font) 
    # 态度
    x,y = (223+138,324)
    color = (0,0,0)           
    size = 16                     
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text1,color,font = font)
    # 好感度差值
    x,y = (223+115,342)
    text = num+"  好感度"       
    color = (0,0,0)           
    size = 16               
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    # ----------------------------------------------------------------------   
    # 时间
    time_local = time.localtime(times)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    x,y = (275,375)
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),str(dt),color,font = font)   
    # 金币
    x,y = (622,266)
    text = str(luck*(int(luck/2))+luck)     
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    if luck > 7:
        text0 = "两倍幸运值！"     
        text = str(2*((8+luck*(int(luck/2)))/100))    
    elif luck > 10:
        text0 = "三倍幸运值！"     
        text = str(3*((8+luck*(int(luck/2)))/100)) 
    else:
        text0 = "额外金币+" + str(luck)
        text = str(((6+luck*(int(luck/2)))/100))     

    # 额外区域        
    x2,y2 = (600,338)
    color = (0,0,0)           
    size = 27                  
    font = './ttf/腾祥爱情体简字体.ttf'
    font = ImageFont.truetype(font,size)
    draw.text((x2,y2),text0,color,font = font)
    # 好感度++
    x,y = (641,240)
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    bg.save('ph.png')

def Evening(qqnum,id,times,luck):
    q_ = json.load(open("./config.json", encoding='utf-8')) # 刷新数据

    # -------------------打开图片创建画板--------------------------
    # 随机选取图片
    path_ =  "./evenings"
    path_list = os.listdir(path_ )
    path_random = choice(path_list)
    image_path = path_+'\\'+path_random
    
    bg = Image.open(image_path)
    draw = ImageDraw.Draw(bg)
    # ------------------------------------------------------------

    # 头像模块----------------------------------------------------
    x, y = 55,251
    box = (x,y, x+100, y+100)
    # 请求头像
    q = requests.get("http://q1.qlogo.cn/g?b=qq&nk="+id+"&s=3" )
    image = Image.open(BytesIO(q.content))
    # 头像和圆形蒙版
    mask = Image.new('RGBA', (100, 100), color=(0,0,0,0)) # 创建一个蒙版
    mask_draw = ImageDraw.Draw(mask) # 在这个蒙板上画的
    mask_draw.ellipse((0,0, 100,100), fill=(0,0,0,255))
    bg.paste(image, box, mask)
    # 头像装饰
    am = Image.open('./decorate/s3.png').convert('RGBA')
    am = am.resize((135,135),Image.ANTIALIAS)
    bg.paste(am, (x-14, y-15),am)
    # -------------------------------------------------------------
    
    # 问候语--------------------------------------------------------
    x = 45
    y = 83
    text = "Evening"
    size = 35
    color = (255,255,255)
    font = './ttf/青鸟华光简魏体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)  
    # 昵称
    x,y = (45,y-59) 
    text = qqnum  
    color = (255,255,255)         
    size = 52 
    font = './ttf/青鸟华光简魏体字体.ttf'                                        
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    # ---------------------------------------------------------------
   
    # 累计天数-------------------------------------------------------
    x,y = (386,165)
    text = str(q_[id]["Sign_in"])
    size = 40        
    color = (211,64,33)
    font = './ttf/腾祥爱情体简字体.ttf'                            
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    (xx,yy) = font.getsize(text)
    # 固定值day
    y = 180
    text = "days"
    size = 30       
    color = (0,0,0)            
    font = './ttf/青鸟华光简魏体字体.ttf'                    
    font = ImageFont.truetype(font,size)
    draw.text((x+8+xx,y),text,color,font = font)
    # ---------------------------------------------------------------

    # 当前好感度
    x,y = (358,221)
    text = str(q_[id]["Favorability"]/100)                
    color = (0,0,0)           
    size = 32                      
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # --------------------------------------------------------------------------
    text_qqi = ["路人","陌生","初识","熟悉","亲近","信赖","爱慕","喜欢","热恋"]
    text_t = ["排斥","警惕","闲聊","在意","想念","唠叨","思念","关注","陪伴"]
    if q_[id]["Favorability"] <=1000:
        text0 =str('0 '+'['+text_qqi[0]+']')
        x0 = int((q_[id]["Favorability"]/1000)*222)
        text1 = text_t[0]
        num = str((1000-q_[id]["Favorability"])/100)
    elif 1000 < q_[id]["Favorability"] <=2500:
        text0 =str('1 '+'['+text_qqi[1]+']')
        x0 = int((q_[id]["Favorability"]/2500)*222)
        text1 = text_t[1]
        num = str((2500-q_[id]["Favorability"])/100)
    elif 2500 < q_[id]["Favorability"] <=5000:
        text0 =str('2 '+'['+text_qqi[2]+']')
        x0 = int((q_[id]["Favorability"]/5000)*222)
        text1 = text_t[2]
        num = str((5000-q_[id]["Favorability"])/100)
    elif 5000 < q_[id]["Favorability"] <=10000:
        text0 =str('3 '+'['+text_qqi[3]+']')
        x0 = int((q_[id]["Favorability"]/10000)*222)
        text1 = text_t[3]
        num = str((10000-q_[id]["Favorability"])/100)
    elif 10000 < q_[id]["Favorability"] <=20000:
        text0 =str('4 '+'['+text_qqi[4]+']')
        x0 = int((q_[id]["Favorability"]/20000)*222)
        text1 = text_t[4]
        num = str((20000-q_[id]["Favorability"])/100)
    elif 20000 < q_[id]["Favorability"] <=30000:
        text0 =str('5 '+'['+text_qqi[5]+']')
        x0 = int((q_[id]["Favorability"]/30000)*222)
        text1 = text_t[5]
        num = str((30000-q_[id]["Favorability"])/100)
    elif 30000 < q_[id]["Favorability"] <=50000:
        text0 =str('6 '+'['+text_qqi[6]+']')
        x0 = int((q_[id]["Favorability"]/50000)*222)
        text1 = text_t[6]
        num = str((50000-q_[id]["Favorability"])/100)        

    # 进度条整体长222 加载覆盖渐变进度条 x0是进度条的数值表现
    img = Image.open('./Gradualchange/Timber.png')
    width, height = img.size
    x = 100
    img_ANTIALIAS = img.resize((x, int(x*height/width)), Image.ANTIALIAS)  # ANTIALIAS 高质量下采样滤波
    box = (0,0, x0, 21)
    region = img_ANTIALIAS.crop(box)
    bg.paste(region,(223,272),region)
    # 好感度
    x,y = (223+108,305) 
    color = (0,0,0)           
    size = 16                     
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text0,color,font = font) 
    # 态度
    x,y = (223+138,324)
    color = (0,0,0)           
    size = 16                     
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text1,color,font = font)
    # 好感度差值
    x,y = (223+115,342)
    text = num+"  好感度"       
    color = (0,0,0)           
    size = 16               
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    # ----------------------------------------------------------------------   
    # 时间
    time_local = time.localtime(times)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    x,y = (275,375)
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),str(dt),color,font = font)   
    # 金币
    x,y = (622,266)
    text = str(luck*(int(luck/2))+luck)     
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    if luck > 7:
        text0 = "两倍幸运值！"     
        text = str(2*((8+luck*(int(luck/2)))/100))    
    elif luck > 10:
        text0 = "三倍幸运值！"     
        text = str(3*((8+luck*(int(luck/2)))/100)) 
    else:
        text0 = "额外金币+" + str(luck)
        text = str(((6+luck*(int(luck/2)))/100))     

    # 额外区域        
    x2,y2 = (600,338)
    color = (0,0,0)           
    size = 27                  
    font = './ttf/腾祥爱情体简字体.ttf'
    font = ImageFont.truetype(font,size)
    draw.text((x2,y2),text0,color,font = font)
    # 好感度++
    x,y = (641,240)
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    bg.save('ph.png')

def Nights(qqnum,id,times,luck):
    
    q_ = json.load(open("./config.json", encoding='utf-8')) # 刷新数据

    # -------------------打开图片创建画板--------------------------
    # 随机选取图片
    path_ =  "./nights"
    path_list = os.listdir(path_ )
    path_random = choice(path_list)
    image_path = path_+'\\'+path_random
    
    bg = Image.open(image_path)
    draw = ImageDraw.Draw(bg)
    # ------------------------------------------------------------

    # 头像模块----------------------------------------------------
    x, y = 55,251
    box = (x,y, x+100, y+100)
    # 请求头像
    q = requests.get("http://q1.qlogo.cn/g?b=qq&nk="+id+"&s=3" )
    image = Image.open(BytesIO(q.content))
    # 头像和圆形蒙版
    mask = Image.new('RGBA', (100, 100), color=(0,0,0,0)) # 创建一个蒙版
    mask_draw = ImageDraw.Draw(mask) # 在这个蒙板上画的
    mask_draw.ellipse((0,0, 100,100), fill=(0,0,0,255))
    bg.paste(image, box, mask)
    # 头像装饰
    am = Image.open('./decorate/s3.png').convert('RGBA')
    am = am.resize((135,135),Image.ANTIALIAS)
    bg.paste(am, (x-14, y-15),am)
    # -------------------------------------------------------------
    
    # 问候语--------------------------------------------------------
    x = 45
    y = 83
    text = "Evening"
    size = 35
    color = (255,255,255)
    font = './ttf/青鸟华光简魏体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)  
    # 昵称
    x,y = (45,y-59) 
    text = qqnum  
    color = (255,255,255)         
    size = 52 
    font = './ttf/青鸟华光简魏体字体.ttf'                                        
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    # ---------------------------------------------------------------
   
    # 累计天数-------------------------------------------------------
    x,y = (386,165)
    text = str(q_[id]["Sign_in"])
    size = 40        
    color = (211,64,33)
    font = './ttf/腾祥爱情体简字体.ttf'                            
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    (xx,yy) = font.getsize(text)
    # 固定值day
    y = 180
    text = "days"
    size = 30       
    color = (0,0,0)            
    font = './ttf/青鸟华光简魏体字体.ttf'                    
    font = ImageFont.truetype(font,size)
    draw.text((x+8+xx,y),text,color,font = font)
    # ---------------------------------------------------------------

    # 当前好感度
    x,y = (358,221)
    text = str(q_[id]["Favorability"]/100)                
    color = (0,0,0)           
    size = 32                      
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # --------------------------------------------------------------------------
    text_qqi = ["路人","陌生","初识","熟悉","亲近","信赖","爱慕","喜欢","热恋"]
    text_t = ["排斥","警惕","闲聊","在意","想念","唠叨","思念","关注","陪伴"]
    if q_[id]["Favorability"] <=1000:
        text0 =str('0 '+'['+text_qqi[0]+']')
        x0 = int((q_[id]["Favorability"]/1000)*222)
        text1 = text_t[0]
        num = str((1000-q_[id]["Favorability"])/100)
    elif 1000 < q_[id]["Favorability"] <=2500:
        text0 =str('1 '+'['+text_qqi[1]+']')
        x0 = int((q_[id]["Favorability"]/2500)*222)
        text1 = text_t[1]
        num = str((2500-q_[id]["Favorability"])/100)
    elif 2500 < q_[id]["Favorability"] <=5000:
        text0 =str('2 '+'['+text_qqi[2]+']')
        x0 = int((q_[id]["Favorability"]/5000)*222)
        text1 = text_t[2]
        num = str((5000-q_[id]["Favorability"])/100)
    elif 5000 < q_[id]["Favorability"] <=10000:
        text0 =str('3 '+'['+text_qqi[3]+']')
        x0 = int((q_[id]["Favorability"]/10000)*222)
        text1 = text_t[3]
        num = str((10000-q_[id]["Favorability"])/100)
    elif 10000 < q_[id]["Favorability"] <=20000:
        text0 =str('4 '+'['+text_qqi[4]+']')
        x0 = int((q_[id]["Favorability"]/20000)*222)
        text1 = text_t[4]
        num = str((20000-q_[id]["Favorability"])/100)
    elif 20000 < q_[id]["Favorability"] <=30000:
        text0 =str('5 '+'['+text_qqi[5]+']')
        x0 = int((q_[id]["Favorability"]/30000)*222)
        text1 = text_t[5]
        num = str((30000-q_[id]["Favorability"])/100)
    elif 30000 < q_[id]["Favorability"] <=50000:
        text0 =str('6 '+'['+text_qqi[6]+']')
        x0 = int((q_[id]["Favorability"]/50000)*222)
        text1 = text_t[6]
        num = str((50000-q_[id]["Favorability"])/100)        

    # 进度条整体长222 加载覆盖渐变进度条 x0是进度条的数值表现
    img = Image.open('./Gradualchange/Evening Sunshine.png')
    width, height = img.size
    x = 100
    img_ANTIALIAS = img.resize((x, int(x*height/width)), Image.ANTIALIAS)  # ANTIALIAS 高质量下采样滤波
    box = (0,0, x0, 21)
    region = img_ANTIALIAS.crop(box)
    bg.paste(region,(223,272),region)
    # 好感度
    x,y = (223+108,305) 
    color = (0,0,0)           
    size = 16                     
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text0,color,font = font) 
    # 态度
    x,y = (223+138,324)
    color = (0,0,0)           
    size = 16                     
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text1,color,font = font)
    # 好感度差值
    x,y = (223+115,342)
    text = num+"  好感度"       
    color = (0,0,0)           
    size = 16               
    font = './ttf/脚印星星字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)
    # ----------------------------------------------------------------------   
    # 时间
    time_local = time.localtime(times)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    x,y = (275,375)
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),str(dt),color,font = font)   
    # 金币
    x,y = (622,266)
    text = str(luck*(int(luck/2))+luck)     
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    if luck > 7:
        text0 = "两倍幸运值！"     
        text = str(2*((8+luck*(int(luck/2)))/100))    
    elif luck > 10:
        text0 = "三倍幸运值！"     
        text = str(3*((8+luck*(int(luck/2)))/100)) 
    else:
        text0 = "额外金币+" + str(luck)
        text = str(((6+luck*(int(luck/2)))/100))     

    # 额外区域        
    x2,y2 = (600,338)
    color = (0,0,0)           
    size = 27                  
    font = './ttf/腾祥爱情体简字体.ttf'
    font = ImageFont.truetype(font,size)
    draw.text((x2,y2),text0,color,font = font)
    # 好感度++
    x,y = (641,240)
    color = (0,0,0)           
    size = 20               
    font = './ttf/腾祥爱情体简字体.ttf'   
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    bg.save('ph.png')

def hallo(qqnum,id,lucks,luck):
    data = json.load(open("./config.json", encoding='utf-8')) # 刷新数据

    # 请求setu模块-----------------------------------------------------
    api = "http://api.btstu.cn/sjbz/?lx=dongman"
    setu = requests.get(api)
    image = Image.open(BytesIO(setu.content))
    width, height = image.size
    # 这里为了小图的判断做了判断
    if width < 1024:
        print("出问题了呢")

    x = 1024
    img_ANTIALIAS = image.resize((x, int(x*height/width)), Image.ANTIALIAS)  # ANTIALIAS 高质量下采样滤波
    width, heights = img_ANTIALIAS.size

    bgm = Image.new('RGB',(1024,heights+950), (0,0,0))
    # -----------------------------------------------------------------

    bg = Image.new('RGB',(1024,950), (255,255,255))
    draw = ImageDraw.Draw(bg)

    # ---------------------------------------时间判断区块-----------------------------------------------------------
    now_time = datetime.datetime.now()  
    start_morning_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '5:00', '%Y-%m-%d%H:%M')
    end_morning_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '11:00', '%Y-%m-%d%H:%M')

    start_noon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '11:00', '%Y-%m-%d%H:%M')
    end_noon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '14:00', '%Y-%m-%d%H:%M')

    start_afternoon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '14:00', '%Y-%m-%d%H:%M')
    end_afternoon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '19:00', '%Y-%m-%d%H:%M')

    start_evening_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '19:00', '%Y-%m-%d%H:%M')
    end_evening_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '23:00', '%Y-%m-%d%H:%M')

    if start_morning_time < now_time < end_morning_time:
        text = "早上好"
    elif start_noon_time < now_time < end_noon_time:
        text = "中午好"
    elif start_afternoon_time < now_time < end_afternoon_time:
        text = "下午好"
    elif start_evening_time < now_time < end_evening_time:
        text = "晚上好"  
    else:
        text = "晚安"

    # 问候语--------------------------------------------------------
    x = 55
    y = 100

    size = 100
    color = (0,0,0)
    font = './ttf/塚源黑体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # 时间----------------------------------------------------------
    time = datetime.datetime.now().strftime('%m-%d')
    text = time
    x0 = 800
    y0 = 100

    size = 70
    color = (102,102,102)
    font = './ttf/塚源黑体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x0,y0),text,color,font = font)

    # @系列----------------------------------------------------------

    text = "@"+qqnum+" 好感度+"+str(lucks/100)+" 硬币+"+str(luck*(int(luck/2))+luck)
    text += "\n已连续签到"+str(data[id]["Signs"])+"天"
    text += "\n已将"+str(luck)+"点能量值转换为好感度"
    text += "\n当前好感度："+str(data[id]["Favorability"]/100)
    text += "\n当前硬币："+str(data[id]["Coin"])

    y = y + 90
    size = 35
    color = (102,102,102)
    font = './ttf/脚印星星字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # 今日运势系列----------------------------------------------------
    text = ["末凶","半凶","小凶","凶","末小吉","末吉","半吉","吉","小吉","中吉","大吉"]

    y = y + 230
    text = "今日运势："+text[luck]
    size = 50
    color = (0,0,0)
    font = './ttf/塚源黑体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    y = y + 70
    text = "★"*(luck+1) + "☆"*(11-(luck+1))
    size = 40
    color = (0,0,0)
    font = './ttf/塚源黑体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # 宜or不宜------------------------------------------------------------

    y = y + 90
    text = "宜\n\n\n\n\n\n不宜"
    size = 50
    color = (0,0,0)
    font = './ttf/塚源黑体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)


    # 具体宜的内容---------------------------------------------------
    path = "./dataworlds/luck"
    with open(path,"r", encoding="utf-8") as f:
        data = f.readlines()
    text = choice(data)
    text += choice(data)

    y = y + 45
    size = 35
    color = (102,102,102)
    font = './ttf/青鸟华光简魏体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # 具体不宜的内容---------------------------------------------------
    path = "./dataworlds/notluck"
    with open(path,"r", encoding="utf-8") as f:
        data = f.readlines()
    # 这里并没有 + \n 似乎出现了问题
    text = choice(data)
    text += choice(data)

    y = y + 155
    size = 35
    color = (102,102,102)
    font = './ttf/青鸟华光简魏体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # 随机生成请勿迷信系列--------------------------------------------------

    text = "随机生成 请勿迷信"
    x = x + 755
    y = y + 90
    size = 20
    color = (102,102,102)
    font = './ttf/脚印星星字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    time = datetime.datetime.now().strftime('%Y')
    text = "NPC_"+time
    x = x + 72
    y = y + 20
    size = 20
    color = (102,102,102)
    font = './ttf/脚印星星字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    bgm.paste(img_ANTIALIAS,(0,0))
    bgm.paste(bg,(0,heights))

    bgm.save('ph0.png')

def goodbay(qqnum,id):

    datas = json.load(open("./config.json", encoding='utf-8')) # 刷新数据

    # 请求setu模块-----------------------------------------------------
    api = "http://api.btstu.cn/sjbz/?lx=dongman"
    setu = requests.get(api)
    image = Image.open(BytesIO(setu.content))
    width, height = image.size
    # 这里为了小图的判断做了判断
    if width < 1024:
        print("出问题了呢")

    x = 1024
    img_ANTIALIAS = image.resize((x, int(x*height/width)), Image.ANTIALIAS)  # ANTIALIAS 高质量下采样滤波
    width, heights = img_ANTIALIAS.size

    bgm = Image.new('RGB',(1024,heights+780), (0,0,0))
    # -----------------------------------------------------------------

    bg = Image.new('RGB',(1024,780), (255,255,255))
    draw = ImageDraw.Draw(bg)

    # ---------------------------------------时间判断区块-----------------------------------------------------------
    now_time = datetime.datetime.now()  
    start_morning_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '5:00', '%Y-%m-%d%H:%M')
    end_morning_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '11:00', '%Y-%m-%d%H:%M')

    start_noon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '11:00', '%Y-%m-%d%H:%M')
    end_noon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '14:00', '%Y-%m-%d%H:%M')

    start_afternoon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '14:00', '%Y-%m-%d%H:%M')
    end_afternoon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '19:00', '%Y-%m-%d%H:%M')

    start_evening_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '19:00', '%Y-%m-%d%H:%M')
    end_evening_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '23:00', '%Y-%m-%d%H:%M')

    if start_morning_time < now_time < end_morning_time:
        text = "早上好"
    elif start_noon_time < now_time < end_noon_time:
        text = "中午好"
    elif start_afternoon_time < now_time < end_afternoon_time:
        text = "下午好"
    elif start_evening_time < now_time < end_evening_time:
        text = "晚上好"  
    else:
        text = "晚安"

    # 问候语--------------------------------------------------------
    x = 55
    y = 100

    size = 100
    color = (0,0,0)
    font = './ttf/塚源黑体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # 时间----------------------------------------------------------
    time = datetime.datetime.now().strftime('%m-%d')
    text = time
    x0 = 800
    y0 = 100

    size = 70
    color = (102,102,102)
    font = './ttf/塚源黑体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x0,y0),text,color,font = font)

    # 网易云时刻-----------------------------------------------------

    #text = "@"+qqnum+" 好感度+"+str(lucks)+" 硬币+"+str(luck*(int(luck/2))+luck)

    path = "./dataworlds/quotations"
    with open(path,"r", encoding="utf-8") as f:
        data = f.readlines()
    
    text = choice(data).split("。")
    print(text)
    text0 = text[0]+'\n'
    text0 += text[1]

    y = y + 110
    size = 45
    color = (102,102,102)
    font = './ttf/脚印星星字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text0,color,font = font)
    # -----------------------------------------------------------------
    
    text = "@" + qqnum + " 今天你已经签到过了哦~"
    text += "\n当前好感度："+str(datas[id]["Favorability"]/100)
    text += "\n当前硬币："+str(datas[id]["Coin"])
    y = y + 150
    size = 45
    color = (102,102,102)
    font = './ttf/脚印星星字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    # 今日运势系列----------------------------------------------------
    text = ["末凶","半凶","小凶","凶","末小吉","末吉","半吉","吉","小吉","中吉","大吉"]
    print(datas[id]["Luck"])
    y = y + 210
    text = "今日运势："+text[datas[id]["Luck"]]
    size = 50
    color = (0,0,0)
    font = './ttf/塚源黑体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    y = y + 65
    text = "★"*(datas[id]["Luck"]+1) + "☆"*(11-(datas[id]["Luck"]+1))
    size = 40
    color = (0,0,0)
    font = './ttf/塚源黑体字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)   

    # 随机生成请勿迷信系列--------------------------------------------------

    text = "随机生成 请勿迷信"
    x = x + 755
    y = y + 60
    size = 20
    color = (102,102,102)
    font = './ttf/脚印星星字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    time = datetime.datetime.now().strftime('%Y')
    text = "NPC_"+time
    x = x + 72
    y = y + 20
    size = 20
    color = (102,102,102)
    font = './ttf/脚印星星字体.ttf'                         
    font = ImageFont.truetype(font,size)
    draw.text((x,y),text,color,font = font)

    bgm.paste(img_ANTIALIAS,(0,0))
    bgm.paste(bg,(0,heights))
    bgm.save('ph1.png')
