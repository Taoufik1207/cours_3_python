import tkinter as tk
from PIL import Image, ImageTk

class Enigme:
    def __init__(self, image_path, enonce, solution, indice):
        self.image_path = image_path
        self.enonce = enonce
        self.solution = solution
        self.indice = indice
class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Énigme Challenge")
        self.geometry("1000x600")

        self.enigmes = [
            Enigme("ressources/villageois1.jpg", "Je suis exploitant agricole et je possède :\n 1/4 d'hectares au nord de la ville,\n 6/8 d'hectares à l'est,\n 3 hectares au sud,\n 24/20 hectares à l'ouest.\n\n Peux tu me dire combien d'hectares je possède au total ?", "5.2", ["Allef lej jool", (4)]),
            Enigme("ressources/villageois2.jpg", "Je suis propriétaire de 3 appartements dont les dimensions sont les suivantes :\n Appt 1 => 16m de long et 8m de large.\n Appt 2 => 12m de long et 10m de large.\n Appt 3 => 15.3m de long et 12.9m de large.\n\n Quelle est la superficie totale de tous mes appartements ?", "445.37", ["daera oào poma ssimss osuonumr cnek ddsea", (3,40, 2)]),
            Enigme("ressources/villageois3.jpg", "Je suis marchand et j'ai reçu 5 paiements dernièrement : \n 2270/90 dh, \n 900/29 dh, \n 3765/123 dh, \n 983/32 dh, \n 4500/2000 dh\n\n Lequel de ces paiements a été le plus élevé ?", "900/29", ["e svlinen fcnh emzp lmrald abnmi", (1,32,2)])
        ]

        self.enigme_actuelle = 0

        self.image_label = tk.Label(self)
        self.image_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.enigme_label = tk.Label(self, text="", wraplength=300, font=("Helvetica", 12))
        self.enigme_label.pack(pady=10)

        self.proposition = tk.Label(self, text="Solution :")
        self.proposition.pack()

        self.reponse_entry = tk.Entry(self)
        self.reponse_entry.pack(pady=5)

        self.check_button = tk.Button(self, text="Vérifier", command=self.verifier_reponse)
        self.check_button.pack(pady=10)

        self.message_label = tk.Label(self, text="")
        self.message_label.pack()

        self.indice_label = tk.Label(self, text="")
        self.indice_label.pack(pady=10)

        self.indice = tk.Label(self, text="", font=("Helvetica", 14, "bold"), wraplength=200)
        self.indice.pack()

        self.suivant_button = tk.Button(self, text="Suivant", command=self.enigme_suivante, state=tk.DISABLED)
        self.suivant_button.pack(pady=10)

        self.felicitations = tk.Label(self, text='', font=("Helvetica", 14, "bold"), fg='green', wraplength=300)
        self.felicitations.pack()

        self.charger_enigme()

    def charger_enigme(self):
        enigme = self.enigmes[self.enigme_actuelle]

        # Charger l'image
        image = Image.open(enigme.image_path)
        nouvelle_dimension = (600, 600)
        image_redimensionnee = image.resize(nouvelle_dimension)
        image_tk = ImageTk.PhotoImage(image_redimensionnee)
        self.image_label.config(image=image_tk)
        self.image_label.image = image_tk

        # Afficher l'énoncé de l'énigme
        self.enigme_label.config(text=enigme.enonce)

    def verifier_reponse(self):
        reponse_utilisateur = self.reponse_entry.get()
        enigme = self.enigmes[self.enigme_actuelle]

        if reponse_utilisateur == enigme.solution:
            self.message_label.config(text="Correct !", fg="green")
            self.indice.config(text=enigme.indice)
            self.indice_label.config(text="Voilà l'indice en ma possession :")
            self.suivant_button.config(state=tk.NORMAL)  # Activer le bouton "Suivant"
        else:
            self.message_label.config(text="Incorrect. Essayez à nouveau.", fg="red")
            self.suivant_button.config(state=tk.DISABLED)  # Désactiver le bouton "Suivant"

    def enigme_suivante(self):
        self.enigme_actuelle += 1
        self.suivant_button.config(state=tk.DISABLED)  # Désactiver le bouton "Suivant" pour la nouvelle énigme
        self.message_label.config(text="")  # Réinitialiser le message
        self.indice.config(text="")
        self.indice_label.config(text="")
        self.reponse_entry.delete(0, tk.END)  # Effacer la réponse précédente

        if self.enigme_actuelle < len(self.enigmes):
            self.charger_enigme()
        else:
            self.felicitations.config(text="Félicitations ! Vous avez résolu toutes les énigmes.")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
