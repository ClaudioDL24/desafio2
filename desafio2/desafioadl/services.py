from .models import Tarea, Subtarea

def recupera_tareas_y_subtareas():
    tareas = Tarea.objects.all()
    datos = []
    for tarea in tareas:
        subtareas = tarea.subtarea_set.all()
        datos.append({'tarea': tarea, 'subtareas': subtareas})
    return datos

def crear_nueva_tarea(descripcion):
    nueva_tarea = Tarea(descripcion=descripcion)
    nueva_tarea.save()
    return recupera_tareas_y_subtareas()

def crear_subtarea(tarea_id, descripcion):
    tarea = Tarea.objects.get(id=tarea_id)
    nueva_subtarea = Subtarea(descripcion=descripcion, tarea=tarea)
    nueva_subtarea.save()
    return recupera_tareas_y_subtareas()

def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return recupera_tareas_y_subtareas()

def elimina_subtarea(subtarea_id):
    subtarea = Subtarea.objects.get(id=subtarea_id)
    subtarea.delete()
    return recupera_tareas_y_subtareas()

def imprimir_en_pantalla(datos):
    for idx, item in enumerate(datos, start=1):
        print(f"[{idx}] {item['tarea'].descripcion}")
        for sub_idx, subtarea in enumerate(item['subtareas'], start=1):
            print(f".... [{idx}.{sub_idx}] {subtarea.descripcion}")
