from zeep import Client

client = Client('http://localhost:7777/ws/AcademicoWebService?wsdl')

def soap_listas(servicio):
    return{
        servicio:client.service.getAllEstudiante()
    }[servicio]

def soap_individual(servicio, parametro):
    if servicio == "asignatura":
        return {servicio:client.service.getAsignatura(parametro)}[servicio]
    elif servicio == "profesor":
        return {servicio:client.service.getProfesor(parametro)}[servicio]

print("Listado de estudiantes")
print(soap_listas("estudiantes"))

print("Asignatura")
print(soap_individual("asignatura", 1))

print("Profesor")
print(soap_individual("profesor", 1))