import datetime
class Empresa:
    def __init__(self,seguro ="Seguro", ID = "001-AD", nombre = "Computon", jefe = "Ing. Anderson Estrda", ruc ="0921171617001", telf ="0982971849", direc ="Bucay (Ganl. Antonio Elizalde"):
        self.nombre = nombre 
        self.ruc = ruc 
        self.jefe = jefe 
        self.telefono = telf 
        self.direccion = direc 
        self.seguro = seguro
        self.ID = ID
    def Departamento(self):
        print("Empresa: {} \nJefe: {:30} Ruc:{}  \nDirecc: {}".format(self.nombre, self.jefe, self.ruc,  self.direccion))
        print("Departamento: {:22} Codigo: {}".format(self.seguro, self.ID))
# hora = datetime.datetime.now()
# print(hora)
# emp = Empresa()
# emp.Departamento()
# print(Empresa())
class Empleado:
    def __init__(self, nom ="Anderson Estrada" , ced ="0921171617", telf ="0982971849", sueldo ="390", Fe_Ingreso= "25/08/2021", comision ="si"):
        self.nombre = nom 
        self.cedula = ced 
        self.telefono = telf
        self.sueldo = sueldo
        self.Fe_Ingreso = Fe_Ingreso
        self.comision = comision
    def comision(self, comi):   # va co sueldo del empleado o al iess
        self.comisiones = comi
        if comision == "si":
            comi = int(input("Ingrese su comision: "))
        elif comision == "no":
            print("Usted no tiene comision")
class Nuevo_Obrero(Empleado): 
    def __init__(self,  nom ="Anderson Estrada" , ced ="0921171617", telf ="0982971849", sueldo ="390", Fe_Ingreso= "25/08/2021", comision ="si",  contrato =None):  
        super().__init__(nom, ced, telf, sueldo, Fe_Ingreso, comision)
        self.contrato = contrato
        if contrato == None:
            "Su contrato es de 3 Meses"
        else:
            "Ya se finalizo su contrato"
class Trabajador(Empleado):
    def __init__(self, nom ="Anderson Estrada" , ced ="0921171617", telf ="0982971849", sueldo ="390", Fe_Ingreso= "25/08/2021", comision ="si", estado = "si", ): 
        super().__init__(nom, ced, telf, sueldo, Fe_Ingreso, comision)
        self.estado = estado 
        if estado == "si":
            self.estado="Activo"
        else:
            return "No Activo"
    def mostrar(self):
        print("Nombre: {:28} C.L.: {:30} \nSueldo BAsico $: {:20} Estado: {} \nFecha Ingreso:{}".format(self.nombre, self.cedula, self.sueldo,self.estado, self.Fe_Ingreso))        
# empl = Empleado()
# empl = Nuevo_Obrero()
# empl = Trabajador()
# empl.mostrar()
# print(Empleado())
class Prestamo(Trabajador):
    def __init__(self, nom ="Anderson Estrada" , ced ="0921171617", sueldo ="390", comision ="si", fecha="3/08/2021", monto ="1000", meses="5", interes="0.10"):
        super().__init__(nom, ced, sueldo, comision)
        self.fecha = fecha
        self.monto = monto
        self.meses = meses
        self.interes = interes 
        # meses = int(input("Ingrese Nro de Meses : "))
    def calculo(self):  
        intereses = 1000 * 5 * 0.10
        total_pago = 1000 + intereses                             # revisar
        print("Nombre: {:22} C.L.: {:20} \nEstado: {:22} Fecha del Prestamo:{}".format(self.nombre, self.cedula, self.estado, self.fecha))    # revisar estado 3 veces     
        print("El valor del Prestamo es $:{:20} \nInteres: {} Pago Total: {:20}".format(self.monto, intereses, total_pago))
# pres = Prestamo()
# pres.calculo()
# print(Prestamo())
class Pago_Salario:
    def __init__(self, pago_hora=15, hora=None, años=None):
        self.pago_hora = pago_hora
        self.hora = hora
        self.años = años
    def calcular(self):
        años = float(input ('Ingresa el valor de antiguedad en años: '))
        hora = float(input ('Ingrese las horas trabajadas: '))
        salario_bruto = hora * 15
        if hora > 30:
           salario_bruto = salario_bruto + (hora - 30) * 15 * 0.5
        if salario_bruto > 390.00:
            impuesto = salario_bruto * 0.1
            print("Su salario es $:{}".format(salario_bruto))
            print("La retencio Para el seguro (IESS) es:{}".format(impuesto))
        else:
            impuesto = salario_bruto * 0.05
            print("Su salario es $:{}".format(salario_bruto))
            print("La retencio Para el seguro (IESS) es:{}".format(impuesto))
        if  años >= 10:
            bonificacion = 150.00
            print("Bonificacion por antiguedad:{}".format(bonificacion))
            salario_neto = salario_bruto - impuesto + bonificacion
            print("Total Ingreso $:{}".format(salario_neto))
        else:
            bonificacion = 0
            salario_neto = salario_bruto - impuesto + bonificacion
            print("Total Ingreso $:{}".format(pagar))
            print("Valor de pago por hora:{}".format(pago_hora))
# pago = Pago_Salario()
# pago.calcular()
# print(Pago_Salario())

     
hora = datetime.datetime.now()
print(hora)
print("******* Nomina Del Trabajador ******")
emp = Empresa()
emp.Departamento()
print(Empresa())
print("--------------------------------------")
empl = Empleado()
empl = Nuevo_Obrero()
empl = Trabajador()
empl.mostrar()
print(Empleado())
print("******Prestamo de Mil dolares*******") 
pres = Prestamo()
pres.calculo()
print(Prestamo())
print("----------------------------------------")
pago = Pago_Salario()
pago.calcular()
print(Pago_Salario())


# Nuevo = input("Desea ingresar a un Trabajador: ")
# if nuevo == "si":
   # nom = input("Ingrese el Nombre del Empleado o Trabajador: ")
   # ced = int(input("Ingrese su numero de cedula: "))
    # telf = int(input("Ingrese su numero telefonico: "))
    # sueldo = int(input("Ingrese su sueldo actual: "))
    # Fe_Ingreso = int(input("Ingrese su fehca de Ingreso a la Empresa: "))           para pedir por teclado
    # sueldo = float(input("Ingrese el salario basico a pagar: "))
    # comision = input("Tiene comision (si) 0 (no): ")