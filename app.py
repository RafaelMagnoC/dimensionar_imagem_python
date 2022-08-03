#importação pacote interno
import os
#importação pacote externo
import cv2

#A função deverá buscar onde as imagens estão armazenadas, salvar todas numa lista, ler cada imagem da lista, cortar cada uma e salvar numa nova pasta de destino.
def dimensionar_imagem(pathRemetente, pathDestinatario):
  #lendo caminho e salvando as imagens numa lista
  lista = os.listdir(pathRemetente)
  #criando um loop para obter cada elemento da lista
  for item in lista:
    #passando o caminho absoluto concatenado com o nome de cada imagem para função
    imagem = cv2.imread(f"{pathRemetente}\{item}")
    #configurando novas dimensões e salvando numa variável
    imagem_dimensionada = imagem[30:140, 30:140]
    #exibindo imagem com novas dimensões (função opcional)
    cv2.imshow("imagem cortada", imagem_dimensionada)
    #salvando imagem dimensionada no destinatário
    cv2.imwrite(f"{pathDestinatario}{item}", imagem_dimensionada)
    #esta função server para aguardar um evento por tecla ou tempo em milissegundos.
    cv2.waitKey(0)

"""
quando executar a função, não esqueça de passar os parâmetros corretamente.
em python, pode passar o intervalo das pastas de três maneiras, deixo abaixo, um exemplo que funciona bem    

Exemplo de função como executar a função:
dimensionar_imagem("C:\\Users\\CISSO-3\\Desktop\\dimensionar-imagens\\imagens", "C:\\Users\\CISSO-3\\Desktop\\dimensionar-imagens\\imagens-dimensionadas\\")

"""