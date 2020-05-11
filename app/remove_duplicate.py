

def dup(n2,g2,s2,u2):
		
		img=[]
		name22=n2
		genre22=g2
		site22=s2
		url_name22=u2
		l1=[]
		l2=[]
		l3=[]
		l4=[]
		l5=[]
		l6=[]
		l7=[]
		l8=[]
		l9=[]
		
		
		
		name1=[]
		name2=[]
		name3=[]
		name4=[]
		name5=[]
		name6=[]
		name7=[]
		name8=[]
		name9=[]
		
		url1=[]
		url2=[]
		url3=[]
		url4=[]
		url5=[]
		url6=[]
		url7=[]
		url8=[]
		url9=[]
		
		site1=[]
		site2=[]
		site3=[]
		site4=[]
		site5=[]
		site6=[]
		site7=[]
		site8=[]
		site9=[]
		
		genre1=[]
		genre2=[]
		genre3=[]
		genre4=[]
		genre5=[]
		genre6=[]
		genre7=[]
		genre8=[]
		genre9=[]
		for x in range(len(site22)):
			if(site22[x]=='NETFLIX'):
				name1.append(name22[x])
				url1.append(url_name22[x])
				site1.append(site22[x])
				genre1.append(site22[x])
				l1.append(x)
			elif(site22[x]=='PRIME'):
				name2.append(name22[x])
				url2.append(url_name22[x])
				site2.append(site22[x])
				genre2.append(site22[x])
				l2.append(x)
			elif(site22[x]=='HOTSTAR'):
				name3.append(name22[x])
				url3.append(url_name22[x])
				site3.append(site22[x])
				genre3.append(site22[x])
				l3.append(x)
			elif(site22[x]=='SONYLIV'):
				name4.append(name22[x])
				url4.append(url_name22[x])
				site4.append(site22[x])
				genre4.append(site22[x])
				l4.append(x)
			elif(site22[x]=='ZEE5'):
				name5.append(name22[x])
				url5.append(url_name22[x])
				site5.append(site22[x])
				genre5.append(site22[x])
				l5.append(x)
			elif(site22[x]=='VOOT'):
				name6.append(name22[x])
				url6.append(url_name22[x])
				site6.append(site22[x])
				genre6.append(site22[x])
				l6.append(x)
			elif(site22[x]=='ALTBALAJI'):
				name7.append(name22[x])
				url7.append(url_name22[x])
				site7.append(site22[x])
				genre7.append(site22[x])
				l7.append(x)
			elif(site22[x]=='EROSNOW'):
				name8.append(name22[x])
				url8.append(url_name22[x])
				site8.append(site22[x])
				genre8.append(site22[x])
				l8.append(x)
			elif(site22[x]=='VIU'):
				name9.append(name22[x])
				url9.append(url_name22[x])
				site9.append(site22[x])
				genre9.append(site22[x])
				l8.append(x)

		
		
		name=[]
		url=[]
		genre=[]
		site=[]
		
		l2=[]
		name_pure=list(dict.fromkeys(name1))
		for j in name_pure:
			l2.append(name1.index(j))
		for i in l2:	
			name.append(name1[i])
			url.append(url1[i])
			genre.append(genre1[i])
			site.append(site1[i])
			img.append('1.png')
		
		
		l2=[]
		name_pure=list(dict.fromkeys(name2))
		for j in name_pure:
			l2.append(name2.index(j))
		for i in l2:	
			name.append(name2[i])
			url.append(url2[i])
			genre.append(genre2[i])
			site.append(site2[i])
			img.append('2.png')
		
		
		l2=[]
		name_pure=list(dict.fromkeys(name3))
		for j in name_pure:
			l2.append(name3.index(j))
		for i in l2:	
			name.append(name3[i])
			url.append(url3[i])
			genre.append(genre3[i])
			site.append(site3[i])
			img.append('8.png')
		l2=[]
		name_pure=list(dict.fromkeys(name4))
		for j in name_pure:
			l2.append(name4.index(j))
		for i in l2:	
			name.append(name4[i])
			url.append(url4[i])
			genre.append(genre4[i])
			site.append(site4[i])
			img.append('4.png')
		l2=[]
		name_pure=list(dict.fromkeys(name5))
		for j in name_pure:
			l2.append(name5.index(j))
		for i in l2:	
			name.append(name5[i])
			url.append(url5[i])
			genre.append(genre5[i])
			site.append(site5[i])
			img.append('6.png')
		l2=[]
		name_pure=list(dict.fromkeys(name6))
		for j in name_pure:
			l2.append(name6.index(j))
		for i in l2:	
			name.append(name6[i])
			url.append(url6[i])
			genre.append(genre6[i])
			site.append(site6[i])
			img.append('7.png')
		l2=[]
		name_pure=list(dict.fromkeys(name7))
		for j in name_pure:
			l2.append(name7.index(j))
		for i in l2:	
			name.append(name7[i])
			url.append(url7[i])
			genre.append(genre7[i])
			site.append(site7[i])
			img.append('5.png')
		l2=[]
		name_pure=list(dict.fromkeys(name8))
		for j in name_pure:
			l2.append(name8.index(j))
		for i in l2:	
			name.append(name8[i])
			url.append(url8[i])
			genre.append(genre8[i])
			site.append(site8[i])
			img.append('3.png')
		l2=[]
		name_pure=list(dict.fromkeys(name9))
		for j in name_pure:
			l2.append(name9.index(j))
		for i in l2:	
			name.append(name9[i])
			url.append(url9[i])
			genre.append(genre9[i])
			site.append(site9[i])
			img.append('9.png')
		
			
		return (url,img,site,name,genre)
