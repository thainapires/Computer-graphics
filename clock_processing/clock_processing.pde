void setup() {
  size(200, 200);
  stroke(255);
  smooth();
}

void draw() {
  int sizeDiv = 100; // 200/2
  int diametro1 = 160; //Primeiro circulo
  int diametro2 = 140; //Segundo circulo
  int raio = diametro1/2;
  
  background(0);
  fill(0,0,102);
  noStroke();

  ellipse(sizeDiv, sizeDiv, diametro1, diametro1); //Desenha o primeiro circulo
  stroke(25); 
  strokeWeight(1);
  ellipse(sizeDiv, sizeDiv, diametro2, diametro2); //Desenha o segundo circulo
  float s = map(second(), 0, 60, 0, TWO_PI) - HALF_PI;
  float m = map(minute(), 0, 60, 0, TWO_PI) - HALF_PI;
  float h = map(hour() % 12, 0, 12, 0, TWO_PI) - HALF_PI;
  
  // Desenhando os ponteiros
  stroke(255);
  strokeWeight(1);
  //Ponteiro de segundos
  line(sizeDiv, sizeDiv, cos(s) * 72 + sizeDiv, sin(s) * 72 + sizeDiv);
  strokeWeight(3);
  //Ponteiro de minutos
  line(sizeDiv, sizeDiv, cos(m) * 60 + sizeDiv, sin(m) * 60 + sizeDiv);
  strokeWeight(5);
  //Ponteiro de horas
  line(sizeDiv, sizeDiv, cos(h) * 50 + sizeDiv, sin(h) * 50 + sizeDiv);


  //Desenha os pontilhados de minutos
  
  for (float f = 0; f < 2*PI; f += 2*PI / 60) {
      float value1 = sizeDiv + cos(f) * (raio-5);
      float value2 = sizeDiv + sin(f) * (raio-5);
      float value3 = sizeDiv + cos(f) * (raio);
      float value4 = sizeDiv + sin(f) * (raio);
      stroke(255, 127, 0);
      strokeWeight(1);
      line(value1, value2, value3, value4);
   }
  
  //Desenha os pontilhados de hora
  for (float f = 0; f < 2*PI; f += 2*PI / 12) {
      float value1 = sizeDiv + cos(f) * (raio-5);
      float value2 = sizeDiv + sin(f) * (raio-5);
      float value3 = sizeDiv + cos(f) * (raio);
      float value4 = sizeDiv + sin(f) * (raio);
      stroke(255, 127, 0);
      strokeWeight(4);
      line(value1,value2, value3, value4);
   }
}
