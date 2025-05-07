import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")


#ANTES DE FILTRAR COMO ANALISTAS DE DATOS DEBES CONOCER (EXPLORAR LA FUENTE PRIMARIA)
#print(dataFrameAsistencia['estado'].unique())
#print(dataFrameAsistencia['estrato'].unique())
print(dataFrameAsistencia['medio_transporte'].unique())

#FILTROS Y CONDICIONES PARA TRANSOFRMAR DATOS
#1. Reportar todos los estudiantes que asistieron
estudiantesQueAsistieron=dataFrameAsistencia.query('estado=="asistio"')
#2. Reportar todos los estudiantes que faltaron
estudiantesQueFaltaron=dataFrameAsistencia.query('estado=="inasistencia"')
#3. Reportar todos los estudiantes que llegaron tarde(Justificado)
estudiantesQueLlegaronTarde=dataFrameAsistencia.query('estado=="justificado"')
#4. Reportar todos los estudiantes de estrato 1
estudiantesEstratoUno=dataFrameAsistencia.query('estrato==1')
#5. Reportar todos los estudiantes de estratos altos
estudiantesEstratoAlto=dataFrameAsistencia.query('estrato!=1 and estrato!=2')
#6. Reportar todos los estudaintes que llegan en metro
estudiantesQueUsanMetro=dataFrameAsistencia.query('medio_transporte=="metro"')
#7. Reportar todos los estudaintes que llegan en bicicleta
estudiantesQueUsanBicicleta=dataFrameAsistencia.query('medio_transporte=="bicicleta"')
#8. Reportar todos los estudiantes que no caminan para llegar a la u
estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_transporte!="a pie"')
#9. Reportar todos los registros de asistencia del mes de junio
estudiantesJunio=dataFrameAsistencia.query('fecha_asistencia.dt.month == 6')
#10. Reportar los estudaintes que faltaron y usan bus para llegar a la u
estudiantesQueFaltanUsanBus=dataFrameAsistencia.query('medio_transporte=="bus" and estado=="inasistencia"')
#11. Reportar estudiantes que usan bus y son de estratos altos
estudiantesQueUsanBusEstratoAlto=dataFrameAsistencia.query('medio_transporte=="bus" and estrato!=1 and estrato!=2')
#12. Reportar estudiantes que usan bus y son de estratos bajos
estudiantesQueUsanBusEstratoBajo=dataFrameAsistencia.query('medio_transporte=="bus" and estrato==1 and estrato==2')
#13. Reportar estudiantes que llegan tarde y son de estrato 3,4,5 o 6
estudiantesQueLleganTardeEstratoAlto=dataFrameAsistencia.query('estado=="justificado" and estrato==3 and estrato==4 and estrato==5 and estrato==6')
#14. Reportar estudiantes que usan transportes ecologicos
estudiantesQueUsanTransporteEcologico=dataFrameAsistencia.query('medio_transporte=="bicicleta" or medio_transporte=="a pie"')
#15. Reportar estudiantes que faltan y usan carro para transportarse
estudiantesQueFaltanUsanCarro=dataFrameAsistencia.query('medio_transporte=="carro" and estado=="inasistencia"')
#16. Reportar estudiantes que asisten son estratos altos y caminan
estudiantesQueAsistenEstratoAltoCaminan=dataFrameAsistencia.query('estado=="asistio" and medio_transporte=="a pie" and estrato!=1 and estrato!=2')
#17. Reportar estudiantes que son estratos bajos y justifican su iniasistencia
estudiantesQueSonEstratosBajosJustifican=dataFrameAsistencia.query('estado=="justificado" and estrato==1 and estrato==2')
#18. Reportar estudiantes que son estratos altos y justifican su iniasistencia
estudiantesQueSonEstratosAltosJustifican=dataFrameAsistencia.query('estado=="justificado" and estrato!=1 and estrato!=2')
#19. Reportar estudiantes que usan carro y justifican su inasistencia
estudiantesQueUsanCarroJustifican=dataFrameAsistencia.query('estado=="justificado" and medio_transporte=="carro"')
#20. Reportar estudiantes que faltan y usan metro y son estratos medios
estudiantesQueFaltanUsanMetroEstratoMedio=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="metro" and estrato==3')
#21. Estudiantes que asistieron y son de estrato 2
estudiantesEstratoDosAsistieron = dataFrameAsistencia.query('estado=="asistio" and estrato==2')
#22. Estudiantes que faltaron sin justificación
estudiantesFaltaronSinJustificar = dataFrameAsistencia.query('estado=="inasistencia" and justificacion==False')
#23. Estudiantes que asistieron y caminan
estudiantesAsistenCaminan = dataFrameAsistencia.query('estado=="asistio" and medio_transporte=="a pie"')
#24. Estudiantes de estrato 3 que usan moto
estudiantesEstrato3Moto = dataFrameAsistencia.query('estrato==3 and medio_transporte=="moto"')
#25. Estudiantes que llegaron tarde sin justificar
estudiantesTardeSinJustificar = dataFrameAsistencia.query('estado=="tarde" and justificacion==False')
#26. Estudiantes de estratos bajos (1-2) que asistieron
estudiantesEstratoBajoAsistieron = dataFrameAsistencia.query('estrato in [1,2] and estado=="asistio"')
#27. Estudiantes de estratos medios (3-4) que faltaron
estudiantesEstratoMedioFaltaron = dataFrameAsistencia.query('estrato in [3,4] and estado=="inasistencia"')
#28. Estudiantes que usan taxi y son de estrato alto (5-6)
estudiantesTaxiEstratoAlto = dataFrameAsistencia.query('medio_transporte=="taxi" and estrato in [5,6]')
#29. Estudiantes que usan taxi y son de estrato bajo (1-2)
estudiantesTaxiEstratoBajo = dataFrameAsistencia.query('medio_transporte=="taxi" and estrato in [1,2]')
#30. Estudiantes que usan moto y son de estrato medio (3-4)
estudiantesMotoEstratoMedio = dataFrameAsistencia.query('medio_transporte=="moto" and estrato in [3,4]')
#31. Estudiantes que usan carro y son de estrato bajo (1-2)
estudiantesCarroEstratoBajo = dataFrameAsistencia.query('medio_transporte=="carro" and estrato in [1,2]')
#32. Estudiantes que usan transporte público (bus o metro)
estudiantesTransportePublico = dataFrameAsistencia.query('medio_transporte in ["bus","metro"]')
#33. Estudiantes que no usan transporte público
estudiantesNoTransportePublico = dataFrameAsistencia.query('medio_transporte not in ["bus","metro"]')
#34. Estudiantes con inasistencias justificadas
estudiantesInasistenciaJustificada = dataFrameAsistencia.query('estado=="inasistencia" and justificacion==True')
#35. Estudiantes con retardos justificados
estudiantesRetardoJustificado = dataFrameAsistencia.query('estado=="tarde" and justificacion==True')
#36. Estudiantes que asistieron en días lluviosos
estudiantesAsistieronLluvia = dataFrameAsistencia.query('estado=="asistio" and clima=="lluvioso"')
#37. Estudiantes que faltaron en días soleados
estudiantesFaltaronSoleado = dataFrameAsistencia.query('estado=="inasistencia" and clima=="soleado"')
#38. Estudiantes de género femenino que asistieron
estudiantesFemeninoAsistieron = dataFrameAsistencia.query('genero=="femenino" and estado=="asistio"')
#39. Estudiantes de género masculino que faltaron
estudiantesMasculinoFaltaron = dataFrameAsistencia.query('genero=="masculino" and estado=="inasistencia"')
#40. Estudiantes que viven a más de 5km y asistieron
estudiantesLejosAsistieron = dataFrameAsistencia.query('distancia > 5 and estado=="asistio"')
#41. Estudiantes que viven cerca (<1km) y faltaron
estudiantesCercaFaltaron = dataFrameAsistencia.query('distancia < 1 and estado=="inasistencia"')
#42. Estudiantes con beca que asistieron
estudiantesBecaAsistieron = dataFrameAsistencia.query('tiene_beca==True and estado=="asistio"')
#43. Estudiantes sin beca que faltaron
estudiantesSinBecaFaltaron = dataFrameAsistencia.query('tiene_beca==False and estado=="inasistencia"')
#44. Estudiantes de primer semestre que asistieron
estudiantesPrimerSemestreAsistieron = dataFrameAsistencia.query('semestre==1 and estado=="asistio"')
#45. Estudiantes de último semestre que faltaron
estudiantesUltimoSemestreFaltaron = dataFrameAsistencia.query('semestre>=10 and estado=="inasistencia"')
#46. Estudiantes con discapacidad que asistieron
estudiantesDiscapacidadAsistieron = dataFrameAsistencia.query('discapacidad==True and estado=="asistio"')
#47. Estudiantes que trabajan y faltaron
estudiantesTrabajanFaltaron = dataFrameAsistencia.query('trabaja==True and estado=="inasistencia"')
#48. Estudiantes que no trabajan y asistieron
estudiantesNoTrabajanAsistieron = dataFrameAsistencia.query('trabaja==False and estado=="asistio"')
#49. Estudiantes con hijos que llegaron tarde
estudiantesConHijosTarde = dataFrameAsistencia.query('tiene_hijos==True and estado=="tarde"')
#50. Estudiantes sin hijos que asistieron
estudiantesSinHijosAsistieron = dataFrameAsistencia.query('tiene_hijos==False and estado=="asistio"')
#51. Estudiantes que viven solos y faltaron
estudiantesVivenSolosFaltaron = dataFrameAsistencia.query('vive_solo==True and estado=="inasistencia"')
#52. Estudiantes que no viven solos y asistieron
estudiantesNoVivenSolosAsistieron = dataFrameAsistencia.query('vive_solo==False and estado=="asistio"')
#53. Estudiantes con promedio alto (>4.0) que asistieron
estudiantesPromedioAltoAsistieron = dataFrameAsistencia.query('promedio > 4.0 and estado=="asistio"')
#54. Estudiantes con promedio bajo (<3.0) que faltaron
estudiantesPromedioBajoFaltaron = dataFrameAsistencia.query('promedio < 3.0 and estado=="inasistencia"')
#55. Estudiantes de ingeniería que asistieron
estudiantesIngenieriaAsistieron = dataFrameAsistencia.query('carrera=="ingenieria" and estado=="asistio"')
#56. Estudiantes de artes que faltaron
estudiantesArtesFaltaron = dataFrameAsistencia.query('carrera=="artes" and estado=="inasistencia"')
#57. Estudiantes internacionales que asistieron
estudiantesInternacionalesAsistieron = dataFrameAsistencia.query('es_internacional==True and estado=="asistio"')
#58. Estudiantes locales que faltaron
estudiantesLocalesFaltaron = dataFrameAsistencia.query('es_internacional==False and estado=="inasistencia"')
#59. Estudiantes que pagan matrícula completa y asistieron
estudiantesPagaCompletaAsistieron = dataFrameAsistencia.query('pago_matricula=="completa" and estado=="asistio"')
#60. Estudiantes con matrícula subsidiada que faltaron
estudiantesMatriculaSubsidiadaFaltaron = dataFrameAsistencia.query('pago_matricula=="subsidiada" and estado=="inasistencia"')
#61. Estudiantes que asistieron a clases tempranas (antes de 10am)
estudiantesAsistieronTemprano = dataFrameAsistencia.query('estado=="asistio" and hora_clase < 10')
#62. Estudiantes que faltaron a clases nocturnas (después de 6pm)
estudiantesFaltaronNocturnas = dataFrameAsistencia.query('estado=="inasistencia" and hora_clase > 18')
#63. Estudiantes que asistieron los lunes
estudiantesAsistieronLunes = dataFrameAsistencia.query('estado=="asistio" and dia_semana=="lunes"')
#64. Estudiantes que faltaron los viernes
estudiantesFaltaronViernes = dataFrameAsistencia.query('estado=="inasistencia" and dia_semana=="viernes"')
#65. Estudiantes que asistieron en la primera quincena
estudiantesAsistieronQuincena1 = dataFrameAsistencia.query('estado=="asistio" and dia_mes <= 15')
#66. Estudiantes que faltaron en la segunda quincena
estudiantesFaltaronQuincena2 = dataFrameAsistencia.query('estado=="inasistencia" and dia_mes > 15')
#67. Estudiantes mayores de 25 años que asistieron
estudiantesMayores25Asistieron = dataFrameAsistencia.query('edad > 25 and estado=="asistio"')
#68. Estudiantes menores de 20 años que faltaron
estudiantesMenores20Faltaron = dataFrameAsistencia.query('edad < 20 and estado=="inasistencia"')
#69. Estudiantes que asistieron y tienen transporte propio
estudiantesTransportePropioAsistieron = dataFrameAsistencia.query('estado=="asistio" and medio_transporte in ["carro","moto"]')
#70. Estudiantes que faltaron y dependen de transporte público
estudiantesTransportePublicoFaltaron = dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte in ["bus","metro"]')
#71. Estudiantes que asistieron a laboratorios
estudiantesAsistieronLaboratorio = dataFrameAsistencia.query('estado=="asistio" and tipo_clase=="laboratorio"')
#72. Estudiantes que faltaron a teóricas
estudiantesFaltaronTeoricas = dataFrameAsistencia.query('estado=="inasistencia" and tipo_clase=="teorica"')
#73. Estudiantes que asistieron a clases con profesor titular
estudiantesAsistieronTitular = dataFrameAsistencia.query('estado=="asistio" and tipo_profesor=="titular"')
#74. Estudiantes que faltaron a clases con profesor auxiliar
estudiantesFaltaronAuxiliar = dataFrameAsistencia.query('estado=="inasistencia" and tipo_profesor=="auxiliar"')
#75. Estudiantes que asistieron a clases obligatorias
estudiantesAsistieronObligatorias = dataFrameAsistencia.query('estado=="asistio" and es_opcional==False')
#76. Estudiantes que faltaron a clases optativas
estudiantesFaltaronOptativas = dataFrameAsistencia.query('estado=="inasistencia" and es_opcional==True')
#77. Estudiantes que asistieron y participaron en clase
estudiantesAsistieronParticiparon = dataFrameAsistencia.query('estado=="asistio" and participacion==True')
#78. Estudiantes que asistieron pero no participaron
estudiantesAsistieronNoParticiparon = dataFrameAsistencia.query('estado=="asistio" and participacion==False')
#79. Estudiantes que faltaron y tienen bajo rendimiento
estudiantesFaltaronBajoRendimiento = dataFrameAsistencia.query('estado=="inasistencia" and rendimiento=="bajo"')
#80. Estudiantes que asistieron y tienen alto rendimiento
estudiantesAsistieronAltoRendimiento = dataFrameAsistencia.query('estado=="asistio" and rendimiento=="alto"')

#AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
#1. Contar cada registro de asistencia por cada estado
conteoRegistrosPorEstado=dataFrameAsistencia.groupby('estado').size()
#2. Numero de registros por estrato
conteoRegistrosPorEstrato=dataFrameAsistencia.groupby('estrato').size()
#3. Cantidad de estudiantes por medio de transporte
conteoEstudiantesPorTransporte=dataFrameAsistencia.groupby('medio_transporte').size()
#4. Cantidad de registros por grupo
conteoRegistrosPorGrupo=dataFrameAsistencia.groupby('grupo').size()
#5. Cruce entre estado y medio de transporte
cruceEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()
#6. Promedio de estrato por estado de asistencia
promedioEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].mean()
print(promedioEstratoPorEstado)
#7. Estrato promedio por medio de transporte
promedioEstratoPorTransporte=dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean()
#8. Maximo estrato por estado de asistencia
maximoEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].max()
#9. Minimo estrato por estado de asistencia
minimoEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].min()
#10.Conteo de asistencias por grupo y por estado
conteoAsistenciasPorGrupoYEstado=dataFrameAsistencia.groupby(['grupo','estado']).size()
#11. Transporte usado por cada grupo
transporteUsadoPorGrupo=dataFrameAsistencia.groupby('grupo')['medio_transporte'].unique()
#12. cuantos grupos distintos registraron asistencia por fecha
conteoGruposPorFecha=dataFrameAsistencia.groupby('fecha_asistencia')['grupo'].nunique()
#13. Promedio de estrato por fecha
promedioEstratoPorFecha=dataFrameAsistencia.groupby('fecha_asistencia')['estrato'].mean()
#14. Numero de tipos de estado por transporte
conteoTiposEstadoPorTransporte=dataFrameAsistencia.groupby('medio_transporte')['estado'].nunique()
#15. Primer Registro de cada grupo
primerRegistroPorGrupo=dataFrameAsistencia.groupby('grupo').first()
#16. Último registro de cada grupo
ultimoRegistroPorGrupo = dataFrameAsistencia.groupby('grupo').last()
#17. Cantidad de estudiantes por grupo
conteoEstudiantesPorGrupo = dataFrameAsistencia.groupby('grupo').size()
#18. Promedio de asistencia por estrato
promedioAsistenciaPorEstrato = dataFrameAsistencia.groupby('estrato')['estado'].mean()
#19. Máximo de asistencia por grupo
maximoAsistenciaPorGrupo = dataFrameAsistencia.groupby('grupo')['estado'].max()
#20. Mínimo de asistencia por grupo
minimoAsistenciaPorGrupo = dataFrameAsistencia.groupby('grupo')['estado'].min()
#21. Número de registros por fecha de asistencia
conteoRegistrosPorFecha = dataFrameAsistencia.groupby('fecha_asistencia').size()
#22. Promedio de asistencia por grupo
promedioAsistenciaPorGrupo = dataFrameAsistencia.groupby('grupo')['estado'].mean()
#23. Número de estudiantes que usan cada medio de transporte
conteoEstudiantesPorMedioTransporte = dataFrameAsistencia.groupby('medio_transporte').size()
#24. Número de registros por estrato y grupo
conteoRegistrosPorEstratoYGrupo = dataFrameAsistencia.groupby(['estrato', 'grupo']).size()
#25. Número de grupos por estrato
conteoGruposPorEstrato = dataFrameAsistencia.groupby('estrato')['grupo'].nunique()
#26. Número de estudiantes por fecha de asistencia
conteoEstudiantesPorFecha = dataFrameAsistencia.groupby('fecha_asistencia').size()
#27. Promedio de fecha de asistencia por grupo
promedioFechaPorGrupo = dataFrameAsistencia.groupby('grupo')['fecha_asistencia'].mean()
#28. Promedio de estrato por fecha
promedioEstratoPorFecha = dataFrameAsistencia.groupby('fecha_asistencia')['estrato'].mean()
#29. Máximo de fecha de asistencia por grupo
maximoFechaPorGrupo = dataFrameAsistencia.groupby('grupo')['fecha_asistencia'].max()
#30. Mínimo de fecha de asistencia por grupo
minimoFechaPorGrupo = dataFrameAsistencia.groupby('grupo')['fecha_asistencia'].min()
#31. Conteo de diferentes tipos de medio de transporte por estado
conteoTiposTransportePorEstado = dataFrameAsistencia.groupby('estado')['medio_transporte'].nunique()
#32. Contar el número de registros de asistencia por estrato y estado
conteoRegistrosPorEstratoYEstado = dataFrameAsistencia.groupby(['estrato', 'estado']).size()
#33. Promedio de transporte por grupo
promedioTransportePorGrupo = dataFrameAsistencia.groupby('grupo')['medio_transporte'].mean()
#34. Cantidad de grupos que usan un medio de transporte específico
conteoGruposPorTransporte = dataFrameAsistencia.groupby('medio_transporte')['grupo'].nunique()
#35. Promedio de asistencia por fecha de grupo
promedioAsistenciaPorFechaYGrupo = dataFrameAsistencia.groupby(['fecha_asistencia', 'grupo'])['estado'].mean()
#36. Número de registros por medio de transporte y estado
conteoRegistrosPorTransporteYEstado = dataFrameAsistencia.groupby(['medio_transporte', 'estado']).size()
#37. Promedio de estrato por transporte y estado
promedioEstratoPorTransporteYEstado = dataFrameAsistencia.groupby(['medio_transporte', 'estado'])['estrato'].mean()
#38. Máximo de estrato por medio de transporte
maximoEstratoPorTransporte = dataFrameAsistencia.groupby('medio_transporte')['estrato'].max()
#39. Mínimo de estrato por medio de transporte
minimoEstratoPorTransporte = dataFrameAsistencia.groupby('medio_transporte')['estrato'].min()
#40. Promedio de estrato por grupo y medio de transporte
promedioEstratoPorGrupoYTransporte = dataFrameAsistencia.groupby(['grupo', 'medio_transporte'])['estrato'].mean()
#41. Número de registros de asistencia por estrato y fecha
conteoRegistrosPorEstratoYFecha = dataFrameAsistencia.groupby(['estrato', 'fecha_asistencia']).size()
#42. Número de registros de asistencia por fecha y estado
conteoRegistrosPorFechaYEstado = dataFrameAsistencia.groupby(['fecha_asistencia', 'estado']).size()
#43. Número de registros de asistencia por grupo y fecha
conteoRegistrosPorGrupoYFecha = dataFrameAsistencia.groupby(['grupo', 'fecha_asistencia']).size()
#44. Promedio de estrato por fecha de asistencia
promedioEstratoPorFechaAsistencia = dataFrameAsistencia.groupby('fecha_asistencia')['estrato'].mean()
#45. Promedio de fecha de asistencia por estrato
promedioFechaPorEstrato = dataFrameAsistencia.groupby('estrato')['fecha_asistencia'].mean()
#46. Promedio de asistencia por medio de transporte
promedioAsistenciaPorTransporte = dataFrameAsistencia.groupby('medio_transporte')['estado'].mean()
#47. Número de estudiantes que asistieron por fecha
conteoEstudiantesPorFechaDeAsistencia = dataFrameAsistencia.groupby('fecha_asistencia')['estado'].sum()
#48. Número de estudiantes que usaron cada transporte por grupo
conteoTransportePorGrupo = dataFrameAsistencia.groupby('grupo')['medio_transporte'].nunique()
#49. Número de registros por medio de transporte y fecha
conteoRegistrosPorTransporteYFecha = dataFrameAsistencia.groupby(['medio_transporte', 'fecha_asistencia']).size()
#50. Promedio de transporte por fecha
promedioTransportePorFecha = dataFrameAsistencia.groupby('fecha_asistencia')['medio_transporte'].mean()
#51. Número de registros de asistencia por grupo y estrato
conteoRegistrosPorGrupoYEstrato = dataFrameAsistencia.groupby(['grupo', 'estrato']).size()
#52. Cantidad de grupos que tienen estudiantes de cada estrato
conteoGruposPorEstrato = dataFrameAsistencia.groupby('estrato')['grupo'].nunique()
#53. Promedio de asistencia por estrato y grupo
promedioAsistenciaPorEstratoYGrupo = dataFrameAsistencia.groupby(['estrato', 'grupo'])['estado'].mean()
#54. Número de registros de asistencia por estrato y transporte
conteoRegistrosPorEstratoYTransporte = dataFrameAsistencia.groupby(['estrato', 'medio_transporte']).size()
#55. Promedio de asistencia por transporte y grupo
promedioAsistenciaPorTransporteYGrupo = dataFrameAsistencia.groupby(['medio_transporte', 'grupo'])['estado'].mean()
#56. Número de registros por grupo y transporte
conteoRegistrosPorGrupoYTransporte = dataFrameAsistencia.groupby(['grupo', 'medio_transporte']).size()
#57. Número de grupos que asistieron a clases por fecha
conteoGruposPorFechaAsistencia = dataFrameAsistencia.groupby('fecha_asistencia')['grupo'].nunique()
#58. Número de estudiantes por estrato y fecha
conteoEstudiantesPorEstratoYFecha = dataFrameAsistencia.groupby(['estrato', 'fecha_asistencia']).size()
#59. Cantidad de asistencia promedio por medio de transporte
promedioAsistenciaPorMedioTransporte = dataFrameAsistencia.groupby('medio_transporte')['estado'].mean()
#60. Promedio de estrato por fecha de transporte
promedioEstratoPorFechaYTransporte = dataFrameAsistencia.groupby(['fecha_asistencia', 'medio_transporte'])['estrato'].mean()
#61. Máximo de asistencia por estrato
maximoAsistenciaPorEstrato = dataFrameAsistencia.groupby('estrato')['estado'].max()
#62. Mínimo de asistencia por estrato
minimoAsistenciaPorEstrato = dataFrameAsistencia.groupby('estrato')['estado'].min()
#63. Número de registros por grupo, estado y fecha
conteoRegistrosPorGrupoEstadoYFecha = dataFrameAsistencia.groupby(['grupo', 'estado', 'fecha_asistencia']).size()
#64. Promedio de fecha de asistencia por estrato y grupo
promedioFechaPorEstratoYGrupo = dataFrameAsistencia.groupby(['estrato', 'grupo'])['fecha_asistencia'].mean()
#65. Número de registros por fecha de asistencia y transporte
conteoRegistrosPorFechaYTransporte = dataFrameAsistencia.groupby(['fecha_asistencia', 'medio_transporte']).size()
#66. Promedio de fecha de asistencia por transporte
promedioFechaPorTransporte = dataFrameAsistencia.groupby('medio_transporte')['fecha_asistencia'].mean()
#67. Promedio de estrato por medio de transporte y estado
promedioEstratoPorTransporteYEstado = dataFrameAsistencia.groupby(['medio_transporte', 'estado'])['estrato'].mean()
#68. Número de registros por grupo, estrato y fecha
conteoRegistrosPorGrupoEstratoYFecha = dataFrameAsistencia.groupby(['grupo', 'estrato', 'fecha_asistencia']).size()
#69. Número de grupos que tienen diferentes medios de transporte
conteoGruposPorTransporteUnico = dataFrameAsistencia.groupby('medio_transporte')['grupo'].nunique()
#70. Número de registros por fecha y estrato
conteoRegistrosPorFechaYEstrato = dataFrameAsistencia.groupby(['fecha_asistencia', 'estrato']).size()
#71. Promedio de asistencia por fecha y medio de transporte
promedioAsistenciaPorFechaYTransporte = dataFrameAsistencia.groupby(['fecha_asistencia', 'medio_transporte'])['estado'].mean()
#72. Número de estudiantes que asistieron por estrato
conteoEstudiantesPorEstrato = dataFrameAsistencia.groupby('estrato')['estado'].sum()
#73. Promedio de estrato por fecha y transporte
promedioEstratoPorFechaYTransporte = dataFrameAsistencia.groupby(['fecha_asistencia', 'medio_transporte'])['estrato'].mean()
#74. Número de grupos que usan más de un medio de transporte
conteoGruposConTransporteUnico = dataFrameAsistencia.groupby('grupo')['medio_transporte'].nunique()
#75. Número de registros de asistencia por grupo, estrato y estado
conteoRegistrosPorGrupoEstratoYEstado = dataFrameAsistencia.groupby(['grupo', 'estrato', 'estado']).size()
#76. Número de registros por estado y grupo
conteoRegistrosPorEstadoYGrupo = dataFrameAsistencia.groupby(['estado', 'grupo']).size()
#77. Promedio de estrato por grupo y fecha
promedioEstratoPorGrupoYFecha = dataFrameAsistencia.groupby(['grupo', 'fecha_asistencia'])['estrato'].mean()
#78. Número de estudiantes por grupo y transporte
conteoEstudiantesPorGrupoYTransporte = dataFrameAsistencia.groupby(['grupo', 'medio_transporte']).size()
#79. Número de grupos por medio de transporte y fecha
conteoGruposPorTransporteYFecha = dataFrameAsistencia.groupby(['medio_transporte', 'fecha_asistencia']).nunique()
#80. Número de registros de asistencia por fecha y grupo
conteoRegistrosPorFechaYGrupo = dataFrameAsistencia.groupby(['fecha_asistencia', 'grupo']).size()