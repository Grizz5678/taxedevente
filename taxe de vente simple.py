# Python permet de recueillir de l'information d'un utilisateur avec une syntaxe relativement simple avec la commande input en combinaison avec
# la définition de la variable (dans ce cas j'ai appelé la variable "achat".)

achat = float(input("Quel est le montant de votre achat assujetti à la taxe de vente harmonisée en Ontario?(en dollars et cents): "))
print("En Ontario, vous aurez à payer ",achat, "dollars +", (achat*.13), " dollars, qui constitue la TVH, ce qui fait un total de",(achat+(achat*.13))," dollars.")