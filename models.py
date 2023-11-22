from django.db import models

# Modelo de departamentos, rige el modelo de empleados

class Departamento(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

# Modelo de empleados, determina la responsabilidad de los equipos

CARGOS = [('Gerente', 'Gerente'), 
          ('Jefe', 'Jefe'),
          ('Coordinador', 'Coordinador'),
          ('Especialista', 'Especialista'),
          ('Supervisor', 'Supervisor'),
          ('Diseñador', 'Diseñador'),
          ('Programador', 'Programador'), 
          ('Soporte', 'Soporte'),
          ('Analista', 'Analista'),]

class Empleado(models.Model):   
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    cargo = models.CharField(choices=CARGOS, max_length=50, default='Sin cargo')
    cedula = models.IntegerField()
    
    def __str__(self):
        return self.nombre

# Computadores y Laptops

class Equipo(models.Model):   
         
    id = models.AutoField(primary_key=True)
    
    # Datos corporativos
    usuario = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    bien_nacional = models.CharField(max_length=6)
    # Datos de fabrica

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    
    procesador = models.CharField(max_length=50)
    ram = models.IntegerField(default=0)
    almacenamiento = models.IntegerField(default=0)
    tipo_disco = models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], max_length=50)
    
    # Datos de Red
    
    ipv4 = models.CharField(max_length=50)
    mac = models.CharField(max_length=50)

    def __str__(self):
        
        if hasattr(self, 'nombre'):
            return self.usuario.nombre
        
        else:
            return self.bien_nacional
# Telefonos celulares    

class Telefono(models.Model):   
    
    id = models.AutoField(primary_key=True)
    
    # Datos corporativos
    
    usuario = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    numero = models.CharField(max_length=50)
    bien_nacional = models.CharField(max_length=6)

    # Datos de fabrica

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)

    # Datos de Red
    
    ipv4 = models.CharField(max_length=50)
    mac = models.CharField(max_length=50)

    def __str__(self):
        
        if hasattr(self, 'nombre'):
            return self.usuario.nombre
        
        else:
            return self.bien_nacional
    
class Impresora(models.Model):
    
    id = models.AutoField(primary_key=True)

    # Datos corporativos
    
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)
    bien_nacional = models.CharField(max_length=6)

    # Datos de fabrica
    
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)

    # Datos de red 
    
    ipv4 = models.CharField(max_length=50)
    mac = models.CharField(max_length=50)
    def __str__(self):
        
        if self.departamento is None:
            return self.ipv4
        
        else:
            return self.ipv4 + ' ' + self.departamento.nombre
    
class Switch(models.Model):
    
    id = models.AutoField(primary_key=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)

    # Datos corporativos
    
    bien_nacional = models.CharField(max_length=6)

    # Datos de fabrica

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    puertos = models.IntegerField(default=0)
    serial = models.CharField(max_length=50)

    # Datos de Red
    
    ipv4 = models.CharField(max_length=50)
    mac = models.CharField(max_length=50)
    def __str__(self):
        return self.ipv4

class Router(models.Model):
    
    id = models.AutoField(primary_key=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)

    # Datos corporativos
    
    bien_nacional = models.CharField(max_length=6)
    
    # Datos de fabrica

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    puertos = models.IntegerField(default=0)
    serial = models.CharField(max_length=50)

    # Datos de Red
    
    ipv4 = models.CharField(max_length=50)
    mac = models.CharField(max_length=50)
    def __str__(self):
        return self.ipv4
    
class Periferico(models.Model):
    
    id = models.AutoField(primary_key=True)
    bien_nacional = models.CharField(max_length=6)
    usuario = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    
    # Datos de fabrica
    
    equipo = models.CharField(choices=[('Monitor', 'Monitor'), ('Mouse', 'Mouse'), ('Teclado', 'Teclado')], max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)

    def __str__(self):
        return self.bien_nacional + self.usuario.nombre
    
# Arreglo de modelos

class NoFuncional(models.Model):
    
    id = models.AutoField(primary_key=True)
    
    # Datos de usuario
    
    bien_nacional = models.CharField(max_length=6)
    
    # Datos corporativos

    usuario = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=100)
    
    # Datos de fabrica
    
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)

    def __str__(self):
        return self.bien_nacional
    
class Solvencia(models.Model):
    
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    
    # Datos de usuario
    bien_nacional = models.CharField(max_length=6)
    
    # Datos corporativos
    usuario = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=100)
    
    # Datos de fabrica
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)

    def __str__(self):
        return self.bien_nacional
    
