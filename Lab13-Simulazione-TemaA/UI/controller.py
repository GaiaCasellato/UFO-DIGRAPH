import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = DAO.getAnnoConAvvistamenti()
        self._listStato = []

    def fillDD(self):
        for i in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(f"{i[0]}-{i[1]}"))
        self._view.update_page()



    def handle_graph(self, e):
        self._view.txt_result.clean()
        self.anno = int((self._view.ddyear.value).split("-")[0])
        self._model.buildGraph(self.anno)
        self._view.txt_result.controls.append(ft.Text(
            f"Numero di vertici: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))
        self._listStato = DAO.getNodi((self._view.ddyear.value).split("-")[0])
        self._view.ddstate.options.clear()
        for i in self._listStato:
            self._view.ddstate.options.append(ft.dropdown.Option(i))

        self._view.update_page()

    def handle_path(self, e):
        pass

    def handle_vicini(self,e):
        tupla1, tupla2 = self._model.vicini(self._view.ddstate.value)
        self._view.txt_result.controls.append(ft.Text(f"Precedenti: "))
        for i in tupla2:
            self._view.txt_result.controls.append(ft.Text(f"{i.id}"))
        self._view.txt_result.controls.append(ft.Text(f"Successori: "))
        for j in tupla1:
            self._view.txt_result.controls.append(ft.Text(f"{j.id}"))

        stato = self._model.idMap[(self._view.ddstate.value).upper()]

        # visited = self._model.getBFSNodes(self._fermataPartenza)
        visited = self._model.getDFSNodes(stato)
        self._view.txt_result.controls.append(
            ft.Text(f"Dalla stato {self._view.ddstate.value} posso raggiungere "
                    f"{len(visited)} stazioni.")
        )
        for v in visited:
            self._view.txt_result.controls.append(ft.Text(v))
        self._view.update_page()