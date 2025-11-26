components = {
    "Battery": "Ceci est une batterie. Un dispositif qui stocke l’énergie chimique et la convertit en énergie électrique. Elle alimente les circuits, microcontrôleurs et autres composants électroniques.",
    "Camera": "Ceci est une caméra. Elle capture des images ou des vidéos pour le traitement visuel. Couramment utilisée en robotique, surveillance ou projets de vision par ordinateur.",
    "Capteur-Gaz": "Ceci est un capteur de gaz. Il détecte la présence ou la concentration de gaz dans l’environnement, utile dans des projets de sécurité comme les détecteurs de fumée ou de fuite de gaz.",
    "DRV8825 driver": "Ceci est un pilote DRV8825. Il contrôle les moteurs pas à pas avec des mouvements précis, largement utilisé dans les imprimantes 3D et la robotique.",
    "Esp": "Ceci est un microcontrôleur ESP. Équipé du Wi-Fi et du Bluetooth, il est idéal pour les projets IoT afin de connecter des appareils à Internet.",
    "GPS": "Ceci est un module GPS. Il reçoit les signaux satellites pour déterminer la position géographique, souvent utilisé dans la navigation et le suivi.",
    "L293D": "Ceci est un pilote L293D. Il permet de contrôler des moteurs à courant continu dans les deux sens, couramment utilisé dans de petits projets robotiques.",
    "LCD-Display": "Ceci est un écran LCD. Il affiche du texte, des nombres ou des graphiques à partir d’un microcontrôleur, utile pour les interfaces utilisateur.",
    "LED": "Ceci est une LED. Une diode électroluminescente qui s’allume lorsqu’elle est alimentée, utilisée pour les indicateurs, signaux ou affichages.",
    "STM": "Ceci est un microcontrôleur STM. Faisant partie de la série STM32, il est utilisé dans les systèmes embarqués offrant de hautes performances et une grande flexibilité.",
    "TB6600 Driver": "Ceci est un pilote TB6600. Il est utilisé pour contrôler de grands moteurs pas à pas avec un courant élevé, souvent dans les machines CNC.",
    "Ultrasonico_sensor": "Ceci est un capteur à ultrasons. Il mesure la distance en envoyant des ondes sonores et en détectant les échos, couramment utilisé pour la détection d’obstacles.",
    "A4988 driver": "Ceci est un pilote A4988. Il contrôle les moteurs pas à pas avec micro-pas pour des mouvements fluides dans de petits projets robotiques ou CNC.",
    "Arduino": "Ceci est une carte Arduino. Une plateforme de microcontrôleur populaire utilisée pour le prototypage en électronique et en robotique.",
    "Board": "Ceci est une carte générique. Elle peut désigner une carte microcontrôleur ou une carte de prototypage utilisée pour assembler des circuits.",
    "DC motor": "Ceci est un moteur à courant continu. Il convertit l’énergie électrique en rotation mécanique, utilisé dans les ventilateurs, roues et actionneurs robotiques.",
    "Display": "Ceci est un écran. Il peut afficher du texte, des graphiques ou des vidéos selon le type, utilisé pour fournir un retour visuel dans les projets.",
    "Multimeter": "Ceci est un multimètre. Un outil pour mesurer la tension, le courant et la résistance dans les circuits électroniques, essentiel pour le dépannage.",
    "Perforated PCB": "Ceci est une carte PCB perforée. Une carte avec des trous pour souder des composants électroniques, utilisée pour le prototypage de circuits.",
    "Rasberry": "Ceci est un Raspberry Pi. Un petit ordinateur monocarte utilisé en robotique, IoT et projets multimédia.",
    "Resistor": "Ceci est une résistance. Elle limite le flux de courant électrique dans un circuit, utilisée pour protéger les composants et contrôler les tensions.",
    "servo Motor": "Ceci est un servomoteur. Un moteur avec un contrôle précis de la position angulaire, couramment utilisé en robotique et automatisation.",
    "Stepper motor": "Ceci est un moteur pas à pas. Il se déplace par pas précis, permettant un positionnement exact, largement utilisé dans les CNC et imprimantes 3D."
}

# Automatically create TXT files for each component
for name, desc in components.items():
    filename = f"{name}-fr.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(desc)

print("✅ All TXT files created with descriptions!")
