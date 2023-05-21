int Pulsador = 2, led1 = 3, led2 = 4, led3 = 5, led4 = 6;
int pot = A0;
int valor;
int randomNumber,fin,inicio,i,j,aux,med1,med2,med3,med4,med5,sA;
String Cantidad,Metodo,Test,Random;

void setup() {
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
  pinMode(led4,OUTPUT);
  pinMode(Pulsador,INPUT_PULLUP);
  Serial.begin(9600);   
  Serial.setTimeout(100);
}

void loop() {
  valor=analogRead(pot);
  valor=map(valor,0,1023,1,4);
  sA=digitalRead(Pulsador)==1?0:1;
  if(valor==1 or valor==2){
    Serial.println(String(valor));
  }
  if(Serial.available()>0){
    String Cadena = Serial.readString();
    if(Cadena=="1"){
    digitalWrite(led1,1);
    digitalWrite(led2,0);
    digitalWrite(led3,0);
    digitalWrite(led4,0);
    }
    else if(Cadena=="2"){
    digitalWrite(led2,1);
    digitalWrite(led1,0);
    digitalWrite(led3,0);
    digitalWrite(led4,0);
    }
    else if(Cadena=="3"){
    digitalWrite(led3,1);
    digitalWrite(led1,0);
    digitalWrite(led2,0);
    digitalWrite(led4,0);
    }
    else if(Cadena=="4"){
    digitalWrite(led4,1);
    digitalWrite(led1,0);
    digitalWrite(led2,0);
    digitalWrite(led3,0);
    }
      
      if (sA==1){
      int inicio=0;
  
      fin = Cadena.indexOf(",",inicio); 
      Cantidad = Cadena.substring(inicio, fin);
      inicio = fin+1;
      fin = Cadena.indexOf(',', inicio);
      Metodo=Cadena.substring(inicio,fin);
      inicio=fin+1;
      fin = Cadena.indexOf(',', inicio);
      Random = Cadena.substring(inicio,fin);
      
      int L1[Cantidad.toInt()];
      int L2[Cantidad.toInt()];
      int L3[Cantidad.toInt()];
      int L4[Cantidad.toInt()];
      int L5[Cantidad.toInt()];
      
      for(i=0;i<Cantidad.toInt();i++){
        randomSeed(random(0,Random.toInt()));
        L1[i]=randomNumber = random(61,101);
        L2[i]=randomNumber = random(60,101);
        L3[i]=randomNumber = random(65,101);
        L4[i]=randomNumber = random(65,101);
        L5[i]=randomNumber = random(21,91);
      }
  
      if(Metodo=="Ninguno"){
        Test=String(L1[0])+","+String(L2[0])+","+String(L3[0])+","+String(L4[0])+","+String(L5[0])+","+"Clase";
        Serial.println(Test);
      }
      
      else if(Metodo=="Promedio"){
        int s1=0,s2=0,s3=0,s4=0,s5=0;
        for(i=0;i<Cantidad.toInt();i++){
          s1=s1+L1[i];
          s2=s2+L2[i];
          s3=s3+L3[i];
          s4=s4+L4[i];
          s5=s5+L5[i];
        }
        s1=s1/Cantidad.toInt();
        s2=s2/Cantidad.toInt();
        s3=s3/Cantidad.toInt();
        s4=s4/Cantidad.toInt();
        s5=s5/Cantidad.toInt();
        Test=String(s1)+","+String(s2)+","+String(s3)+","+String(s4)+","+String(s5)+","+"Clase";
        Serial.println(Test);
      }
      
      else if(Metodo=="Mediana"){
        for(i=0;i<Cantidad.toInt()-1;i++){
          for(j=0;j<Cantidad.toInt()-i-1;j++){
            
            if(L1[j+1]<L1[j]){
              aux = L1[j + 1];
              L1[j + 1] = L1[j];
              L1[j] = aux;
            }
  
            if(L2[j+1]<L2[j]){
              aux = L2[j + 1];
              L2[j + 1] = L2[j];
              L2[j] = aux;
            }
  
            if(L3[j+1]<L3[j]){
              aux = L3[j + 1];
              L3[j + 1] = L3[j];
              L3[j] = aux;
            }
  
            if(L4[j+1]<L4[j]){
              aux = L4[j + 1];
              L4[j + 1] = L4[j];
              L4[j] = aux;
            }
  
            if(L5[j+1]<L5[j]){
              aux = L5[j + 1];
              L5[j + 1] = L5[j];
              L5[j] = aux;
            }
          }
        }
        
        if(Cantidad.toInt()%2==0){
          med1=((L1[Cantidad.toInt()/2]+L1[(Cantidad.toInt()/2)-1])/2);
          med2=((L2[Cantidad.toInt()/2]+L2[(Cantidad.toInt()/2)-1])/2);
          med3=((L3[Cantidad.toInt()/2]+L3[(Cantidad.toInt()/2)-1])/2);
          med4=((L4[Cantidad.toInt()/2]+L4[(Cantidad.toInt()/2)-1])/2);
          med5=((L5[Cantidad.toInt()/2]+L5[(Cantidad.toInt()/2)-1])/2);
        }else{
          med1=L1[int(Cantidad.toInt()/2)];
          med2=L2[int(Cantidad.toInt()/2)];
          med3=L3[int(Cantidad.toInt()/2)];
          med4=L4[int(Cantidad.toInt()/2)];
          med5=L5[int(Cantidad.toInt()/2)];
        }
        Test=String(med1)+","+String(med2)+","+String(med3)+","+String(med4)+","+String(med5)+","+"Clase";
        Serial.println(Test);
      }
  
      else if(Metodo=="Moda"){
        for(i=0;i<Cantidad.toInt()-1;i++){
          for(j=0;j<Cantidad.toInt()-i-1;j++){
            
            if(L1[j+1]<L1[j]){
              aux = L1[j + 1];
              L1[j + 1] = L1[j];
              L1[j] = aux;
            }
  
            if(L2[j+1]<L2[j]){
              aux = L2[j + 1];
              L2[j + 1] = L2[j];
              L2[j] = aux;
            }
  
            if(L3[j+1]<L3[j]){
              aux = L3[j + 1];
              L3[j + 1] = L3[j];
              L3[j] = aux;
            }
  
            if(L4[j+1]<L4[j]){
              aux = L4[j + 1];
              L4[j + 1] = L4[j];
              L4[j] = aux;
            }
  
            if(L5[j+1]<L5[j]){
              aux = L5[j + 1];
              L5[j + 1] = L5[j];
              L5[j] = aux;
            }
          }
        }
  
        int cont1=1,cont2=1,cont3=1,cont4=1,cont5=1;
        int may1=0,mod1=0,may2=0,mod2=0,may3=0,mod3=0,may4=0,mod4=0,may5=0,mod5=0;
        
        for(i=0;i<Cantidad.toInt()-1;i++){
          
          if(L1[i]==L1[i+1]){
            cont1+=1;
          }
          else if(cont1>may1){
              mod1=L1[i];
              may1=cont1;
            }
            cont1=1;
  
          if(L2[i]==L2[i+1]){
            cont2+=1;
          }
          else if(cont2>may2){
              mod2=L2[i];
              may2=cont2;
            }
            cont2=1;
  
          if(L3[i]==L3[i+1]){
            cont3+=1;
          }
          else if(cont3>may3){
              mod3=L3[i];
              may3=cont3;
            }
            cont3=1;
  
          if(L4[i]==L4[i+1]){
            cont4+=1;
          }
          else if(cont4>may4){
              mod4=L4[i];
              may4=cont4;
            }
            cont4=1;
  
          if(L5[i]==L5[i+1]){
            cont5+=1;
          }
          else if(cont5>may5){
              mod5=L5[i];
              may5=cont5;
            }
            cont5=1;
            
          }
          Test=String(mod1)+","+String(mod2)+","+String(mod3)+","+String(mod4)+","+String(mod5)+","+"Clase";
          Serial.println(Test);
        }
  
      else{
        for(i=0;i<Cantidad.toInt()-1;i++){
          for(j=0;j<Cantidad.toInt()-i-1;j++){
            
            if(L1[j+1]<L1[j]){
              aux = L1[j + 1];
              L1[j + 1] = L1[j];
              L1[j] = aux;
            }
  
            if(L2[j+1]<L2[j]){
              aux = L2[j + 1];
              L2[j + 1] = L2[j];
              L2[j] = aux;
            }
  
            if(L3[j+1]<L3[j]){
              aux = L3[j + 1];
              L3[j + 1] = L3[j];
              L3[j] = aux;
            }
  
            if(L4[j+1]<L4[j]){
              aux = L4[j + 1];
              L4[j + 1] = L4[j];
              L4[j] = aux;
            }
  
            if(L5[j+1]<L5[j]){
              aux = L5[j + 1];
              L5[j + 1] = L5[j];
              L5[j] = aux;
            }
          }
        }
          
        if(Metodo=="Minimo"){
          Test=String(L1[0])+","+String(L2[0])+","+String(L3[0])+","+String(L4[0])+","+String(L5[0])+","+"Clase";
          Serial.println(Test);
        }
        else if(Metodo=="Maximo"){
          Test=String(L1[Cantidad.toInt()-1])+","+String(L2[Cantidad.toInt()-1])+","+String(L3[Cantidad.toInt()-1])+","+String(L4[Cantidad.toInt()-1])+","+String(L5[Cantidad.toInt()-1])+","+"Clase";
          Serial.println(Test);
        }
      }
    }
  }
 delay(100);
}
