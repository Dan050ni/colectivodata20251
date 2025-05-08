#1. Solo estudiantes
import pandas as df

dataFrameAsistencia=df.read_csv("./data/asistencia_estudiantes_completo.csv")


soloEstudiantes = df.query('tipo == "estudiante"')

#2. Solo profesores
soloProfesores = df.query('tipo == "profesor"')

#3. Todos excepto estudiantes
noEstudiantes = df.query('tipo != "estudiante"')

#4. Filtrar por especialidad
especialidadFiltrada = df.query('especialidad == "Programación"')  # Reemplaza con la especialidad deseada

#5. Excluir una especialidad
sinEspecialidadX = df.query('especialidad != "Redes"')  # Reemplaza con la especialidad a excluir

#6. Excluir administrativos
sinAdministrativos = df.query('tipo != "administrativo"')

#7. Direcciones en Medellín
enMedellin = df.query('direccion.str.contains("medellin", case=False)', engine='python')

#8. Direcciones terminadas en "sur"
terminanEnSur = df.query('direccion.str.endswith("sur")', engine='python')

#9. Direcciones que inician con "calle"
inicianConCalle = df.query('direccion.str.lower().str.startswith("calle")', engine="python")

#10. Especialidades que contienen la palabra "datos"
conDatos = df.query('especialidad.str.contains("datos", case=False)', engine='python')

#11. Instructores en Itagüí
instructoresItagui = df.query('(tipo == "instructor") and (direccion.str.contains("itagui", case=False))', engine='python')

#12. Nacidos después del 2000
nacidosDespues2000 = df.query('fecha_nacimiento > "2000-01-01"')

#13. Nacidos en los 90
nacidosEn90s = df.query('(fecha_nacimiento >= "1990-01-01") and (fecha_nacimiento <= "1999-12-31")')

#14. Direcciones en Envigado
enEnvigado = df.query('direccion.str.contains("envigado", case=False)', engine='python')

#15. Especialidades que empiezan por "I"
especialidadesConI = df.query('especialidad.str.startswith("I")', engine='python')

#16. Usuarios sin dirección
sinDireccion = df.query('direccion.isnull() or direccion == ""')

#17. Usuarios sin especialidad
sinEspecialidad = df.query('especialidad.isnull() or especialidad == ""')

#18. Profesores que viven en Sabaneta
profesoresSabaneta = df.query('(tipo == "profesor") and direccion.str.contains("sabaneta", case=False)', engine='python')

#19. Aprendices que viven en Bello
aprendicesBello = df.query('(tipo == "aprendiz") and direccion.str.contains("bello", case=False)', engine='python')

#20. Nacidos en el nuevo milenio (desde 2000)
nacidosNuevoMilenio = df.query('fecha_nacimiento >= "2000-01-01"')


#1. Total por tipo
totalPorTipo = df['tipo'].value_counts()

#2. Total por especialidad
totalPorEspecialidad = df['especialidad'].value_counts()

#3. Cantidad de especialidades distintas
especialidadesDistintas = df['especialidad'].nunique()

#4. Tipos de usuario por especialidad
tiposPorEspecialidad = df.groupby('especialidad')['tipo'].value_counts()

#5. Usuario más antiguo por tipo (más edad)
df['edad'] = df.to_datetime('today').year - df.to_datetime(df['fecha_nacimiento']).dt.year
masAntiguoPorTipo = df.sort_values('edad', ascending=False).groupby('tipo').first()

#6. Usuario más joven por tipo
masJovenPorTipo = df.sort_values('edad').groupby('tipo').first()

#7. Primer registro por tipo
primerRegistro = df.groupby('tipo').first()

#8. Último registro por tipo
ultimoRegistro = df.groupby('tipo').last()

#9. Combinación tipo por especialidad
combinacionTipoEspecialidad = df.groupby(['especialidad', 'tipo']).size()

#10. El más viejo por especialidad
masViejoPorEspecialidad = df.sort_values('edad', ascending=False).groupby('especialidad').first()

#11. Cuántos de cada especialidad por tipo
conteoEspecialidadTipo = df.groupby(['tipo', 'especialidad']).size()

#12. Edad promedio por tipo
edadPromedioPorTipo = df.groupby('tipo')['edad'].mean()

#13. Años de nacimiento más frecuente por especialidad
df['año_nacimiento'] = df.to_datetime(df['fecha_nacimiento']).dt.year
anioMasFrecuente = df.groupby('especialidad')['año_nacimiento'].agg(lambda x: x.mode()[0])

#14. Mes de nacimiento más frecuente por tipo
df['mes_nacimiento'] = df.to_datetime(df['fecha_nacimiento']).dt.month
mesMasFrecuente = df.groupby('tipo')['mes_nacimiento'].agg(lambda x: x.mode()[0])

#15. Consulta propuesta: Estudiantes de "Big Data" nacidos después del 2000
estudiantesBigData2000 = df.query('(tipo == "estudiante") and (especialidad.str.contains("big data", case=False)) and (fecha_nacimiento > "2000-01-01")', engine='python')
