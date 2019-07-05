import png

reader = png.Reader(filename='Vd-Orig.png')
w, h, pixels, metadata = reader.read_flat()

if(metadata['alpha']):
	bytesPerPixel = 4
else:
	bytesPerPixel = 3
    
print("bytesPerPixel: ", bytesPerPixel)

matriz = [-1,-1,-1, -1,8,-1, -1,-1,-1]
#matriz = [0,0,0, 0,1,0, 0,0,0]
#matriz = [0,-1,0, -1,5,-1, 0,-1,0]
#matriz = [1,0,-1, 0,0,0, -1,0,1]

imagemNova = [0,0,0] * w * h

for linha in range(0,h):
	for coluna in range(0,w):
		acc =0
		try:

			posicao_superior = bytesPerPixel*(w*(linha-1)+coluna)
			posicao_central = bytesPerPixel*(w*linha+coluna)
			posicao_inferior = bytesPerPixel*(w*(linha+1)+coluna)
            
			posicao = posicao_superior
			acc += pixels[posicao] * matriz[0]
			acc += pixels[posicao+bytesPerPixel] * matriz[1]
			acc += pixels[posicao+bytesPerPixel*2] * matriz[2]
			
			posicao = posicao_central
			acc += pixels[posicao] * matriz[3]
			acc += pixels[posicao+bytesPerPixel] * matriz[4]
			acc += pixels[posicao+bytesPerPixel*2] * matriz[5]
			
			posicao = posicao_inferior
			acc += pixels[posicao] * matriz[6]
			acc += pixels[posicao+bytesPerPixel] * matriz[7]
			acc += pixels[posicao+bytesPerPixel*2] * matriz[8]           
			posicao = posicao_central
			if abs(acc) > 255:
				acc = 255
			imagemNova[posicao] = abs(acc)
			imagemNova[posicao+1] = abs(acc)
			imagemNova[posicao+2] = abs(acc)

		except:
			pass

output = open('Vd-Orig_modificada.png', 'wb')
writer = png.Writer(w, h, **metadata)
writer.write_array(output, imagemNova)
output.close()
