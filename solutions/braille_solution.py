
#Question link - https://github.com/rudisimo/google-foobar/blob/master/challenges/l1-braille-translation-2.md

#Answer-
def get_ascii(text_val):
	ans=''
	ascii_vals = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
	braille = [ '000000', '100000', '110000', '100100', '100110', '100010', '110100', '110110', '110010', '010100', '010110', '101000', '111000', '101100', '101110', '101010', '111100', '111110', '111010', '011100', '011110', '101001', '111001', '010111', '101101', '101111', '101011'] 	
	for i in range(0,len(text_val)):
		if(text_val[i].isupper()):
			ans=ans+'000001'
		ans=ans+braille[ascii_vals.index(text_val[i].lower())]
	return ans

if __name__ =='__main__':
	plaintext = input()
	answer = get_ascii(plaintext)
	print(answer)

