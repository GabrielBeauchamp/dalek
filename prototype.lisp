(defstruct joueur
  x
  y
  zap-count
  has-zap)

(defstruct dalek
  x
  y)

(defparameter *x* 20 "Taille en X de l'arene")
(defparameter *y* 20 "Taille en Y de l'arene")
(defvar *daleks* ())
(defvar *joueurs* (make-joueur :x (random *x*) :y (random *y*)))

(defun dalek-deplacement (dalek joueur)
  "Effectue le deplacement vers le JOUEUR"
  (cond
    ((> (dalek-x dalek) (joueur-x joueur)) 
     (decf (dalek-x dalek)))
    ((< (dalek-x dalek) (joueur-x joueur)) 
     (incf (dalek-x dalek))))
  (cond
    ((> (dalek-y dalek) (joueur-y joueur)) 
     (decf (dalek-y dalek)))
    ((< (dalek-y dalek) (joueur-y joueur)) 
     (incf (dalek-y dalek)))))

(defun init-dalek (n)
  "Rajoute N daleks a la liste *DALEKS* avec une position RANDOM." 
  (loop for i from 1 to n
       do (push (make-dalek :x (random *x*) :y (random *y*)) *daleks*)))

(defun deplace-daleks ()
  "Deplace les daleks vers le joueur"
  (loop for i in *daleks*
       do (dalek-deplacement i *joueurs*)))

(defun deplacement-valide-p (touche)
  "Prend un char et teste pour savoir si la touche est bonne."
  (case touche
    (#\j t)				;A la vim
    (#\k t)
    (#\l t)
    (#\h t)
    (#\y t)
    (#\u t)
    (#\b t)
    (#\n t)
    (#\w t)				;A la fps
    (#\a t)
    (#\s t)
    (#\d t)))

(defun touche-valide-p (touche)
  "Teste pour savoir si la touche est valide."
  (or (deplacement-valide-p touche)
      (case touche
	(#\z t)				;zap
	(#\t t)				;teleport
	(#\q t))))			;quit

;; (defun teleporte (joueur)
;;   "Teleporte un joueur a un point safe."
;;   ())

;; (defun affiche-jeu ()
;;   (loop for i from 1 upto *y*
;;      do (loop for j from 1 upto *x*
;; 	   do

