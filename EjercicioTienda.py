#Tienda de Supermercado
cantidad_leche = 20
precio_leche=1.19
total_lecheu=0


cantidad_galletas= 32
precio_galletas= 1.45
total_galletasu=0


cantidad_mantequilla= 15
precio_mantequilla=1.90
total_mantequillau=0


cantidad_queso=15
precio_queso=2.59
total_quesou=0


cantidad_pan=20
precio_pan=4.99
total_panu=0


cantidad_jalea=18
precio_jalea=3.65
total_jaleau=0


cantidad_yogurt=35
precio_yogurt=3.15
total_yogurtu=0


cantidad_manzanas=35
precio_manzanas=2.15
total_manzanasu=0


cantidad_naranjas=40
precio_naranjas=0.99
total_naranjasu=0


cantidad_bananos=23
precio_bananos=1.29
total_bananosu=0

cuenta_usuario=0



print("Ingrese su nombre")
nombre_usuario = input("Nombre y Apellido: ")
num_producto = 0

while(num_producto != 13):
    print("MENU: (1)leche, (2)galletas, (3)mantequilla, (4)queso, (5)pan, (6)Jalea, (7)Yogurt, (8)Manzanas, (9)Naranjas, (10)Bananos, (12)ver total, (13)Salir")

    num_producto = int(input("Ingrese numero de producto/opción: "))

    if (num_producto == 1):
        ##print("¿Cuantos botes de leche desea?")
        cantidad_leche_u = int(input("¿Cuantos botes de leche desea?: "))
        
        if cantidad_leche_u > 20:
            print("cantidad no disponible en existencia")
        
        else:
            cantidad_leche = cantidad_leche - cantidad_leche_u
            total_lecheu = cuenta_usuario + (cantidad_leche_u * precio_leche)
            
            print("su total es:" + str(total_lecheu))
            print ("Cantidad de leche disponible " + str(cantidad_leche))
    
    if (num_producto == 2):
    ##print("¿Cuantos botes de leche desea?")
        cantidad_galletas_u = int(input("¿Cuantos paquetes de galletas desea?: "))
        
        if cantidad_galletas_u > 32:
            print("cantidad no disponible en existencia")
        
        else:
            cantidad_galletas = cantidad_galletas - cantidad_galletas_u
            total_galletasu = cuenta_usuario + (cantidad_galletas_u * precio_galletas)
                
            print(nombre_usuario + " su total es:" + str(total_galletasu))
            print ("Cantidad de galletas disponible " + str(cantidad_galletas))
    
    if (num_producto == 3):
        ##print("¿Cuantos botes de leche desea?")
        cantidad_mantequilla_u = int(input("¿Cuantos paquetes de mantequilla desea?: "))
        
        if cantidad_mantequilla_u > 15:
            print("cantidad no disponible en existencia")
        
        else:
            cantidad_mantequilla = cantidad_mantequilla - cantidad_mantequilla_u
            total_mantequillau = cuenta_usuario + (cantidad_mantequilla_u * precio_mantequilla)
                
            print("su total es:" + str(total_mantequillau))
            print ("Cantidad de mantequilla disponible " + str(cantidad_mantequilla))
    
    if (num_producto == 4):
        ##print("¿Cuantos botes de leche desea?")
        cantidad_queso_u = int(input("¿Cuantos paquetes de queso desea?: "))
        
        if cantidad_queso_u > 15:
            print("cantidad no disponible en existencia")
        
        else:
            cantidad_queso = cantidad_queso - cantidad_queso_u
            total_quesou = cuenta_usuario + (cantidad_queso_u * precio_queso)
                
            print("su total es:" + str(total_quesou))
            print ("Cantidad de queso disponible " + str(cantidad_queso))
        
    
    if (num_producto == 5):
        ##print("¿Cuantos botes de leche desea?")
        cantidad_pan_u = int(input("¿Cuantos paquetes de pan desea?: "))
        
        if cantidad_pan_u > 20:
            print("cantidad no disponible en existencia")
        
        else:
            cantidad_pan = cantidad_pan - cantidad_pan_u
            total_panu = cuenta_usuario + (cantidad_pan_u * precio_pan)
                
            print("su total es:" + str(total_panu))
            print ("Cantidad de pan disponible " + str(cantidad_pan))
    
    if (num_producto == 6):
        ##print("¿Cuantos botes de leche desea?")
        cantidad_jalea_u = int(input("¿Cuantos tarros de jalea desea?: "))
        
        if cantidad_jalea_u > 18:
            print("cantidad no disponible en existencia")
        
        else:
            cantidad_jalea= cantidad_jalea - cantidad_jalea_u
            total_jaleau = cuenta_usuario + (cantidad_jalea_u * precio_jalea)
                
            print("su total es:" + str(total_mantequillau))
            print ("Cantidad de jalea disponible " + str(cantidad_jalea))
            
            
    if (num_producto == 7):
        ##print("¿Cuantos botes de leche desea?")
        cantidad_yogurt_u = int(input("¿Cuantos botes de yogurt desea?: "))
        
        if cantidad_yogurt_u > 35:
            print("cantidad no disponible en existencia")
        
        else:
            cantidad_yogurt = cantidad_yogurt - cantidad_yogurt_u
            total_yogurtu = cuenta_usuario + (cantidad_yogurt_u * precio_yogurt)
                
            print("su total es:" + str(total_mantequillau))
            print ("Cantidad de queso disponible " + str(cantidad_queso))
            
                   
    if (num_producto == 8):
        ##print("¿Cuantos botes de leche desea?")
        cantidad_manzanas_u = int(input("¿Cuantas manzanas desea?: "))
        
        if cantidad_manzanas_u > 35:
            print("cantidad no disponible en existencia")
        
        else:
            cantidad_manzanas = cantidad_manzanas - cantidad_manzanas_u
            total_manzanasu = cuenta_usuario + (cantidad_manzanas_u * precio_manzanas)
                
            print("su total es:" + str(total_manzanasu))
            print ("Cantidad de manzanas disponible " + str(cantidad_manzanas))
            
            

    if (num_producto == 9):
        ##print("¿Cuantos botes de leche desea?")
        cantidad_naranjas_u = int(input("¿Cuantas Naranjas desea?: "))
        
        if cantidad_naranjas_u > 40:
            print("cantidad no disponible en existencia")
        
        else:
            cantidad_naranjas = cantidad_naranjas - cantidad_naranjas_u
            total_naranjasu = cuenta_usuario + (cantidad_naranjas_u * precio_naranjas)
                
            print("su total es:" + str(total_naranjasu))
            print ("Cantidad de naranjas disponible " + str(cantidad_naranjas))
        
        
        
    if (num_producto == 10):
        ##print("¿Cuantos botes de leche desea?")
        cantidad_bananos_u = int(input("¿Cuantos bananos desea?: "))
        
        if cantidad_bananos_u > 23:
            print("cantidad no disponible en existencia")
        
        else:
            cantidad_bananos = cantidad_bananos - cantidad_bananos_u
            total_bananosu = cuenta_usuario + (cantidad_bananos_u * precio_bananos)
                
            print("su total es:" + str(total_bananosu))
            print ("Cantidad de bananos disponible " + str(cantidad_bananos))
                    
                    
    if (num_producto == 12):
        totalfinal= total_lecheu + total_mantequillau + total_galletasu + total_quesou + total_panu + total_jaleau + total_yogurtu + total_manzanasu + total_naranjasu + total_bananosu
        print(nombre_usuario + " su total final es " + str(totalfinal))
  
    

        

