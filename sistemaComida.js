
// CLASE PADRE: Comida
// Esta es la clase principal que define lo básico de cualquier comida

class Comida {
    constructor(nombre, precio, paisOrigen) {
        this.nombre = nombre;
        this.precio = precio;
        this.paisOrigen = paisOrigen;
    }

    // Metodo para describir la comida
     // Lo uso para mostrar informacion general del platillo
    describir() {
        return `${this.nombre} - $${this.precio} (${this.paisOrigen})`;
    }

    // Metodo para preparar la comida
    // Todas las comidas se pueden preparar, por eso esta en la clase padre

    preparar() {
        console.log(` Preparando ${this.nombre}...`);
    }
}


// CLASE HIJA: Postre
// Hereda de Comida y agrega caracteristicas especificas de postres
// Con super() llamo al constructor de la clase padre (Comida)
// Así no tengo que repetir nombre, precio y paisOrigen
class Postre extends Comida {
    constructor(nombre, precio, paisOrigen, esDulce, temperatura) {
        super(nombre, precio, paisOrigen);
        this.esDulce = esDulce;  // Si es dulce o no (true/false)
        this.temperatura = temperatura; // frio o caliente
    }

    // Metodo propio de Postre
    // Los platos fuertes no tienen este metodo

    servir() {
        console.log(` Sirviendo ${this.nombre} ${this.temperatura}`);
    }

    // Sobrescribo el metodo describir() de la clase padre
    // Agrego informacion especifica de postres

    describir() {
        return `${super.describir()} - ${this.esDulce ? 'Dulce' : 'No dulce'} - ${this.temperatura}`;
    }
}


// CLASE HIJA: PlatoFuerte 
// Hereda de Comida y agrega caracteristicas de platos principales
class PlatoFuerte extends Comida {
    constructor(nombre, precio, paisOrigen, tipoCarne, picante) {
        super(nombre, precio, paisOrigen);
        this.tipoCarne = tipoCarne;
        this.picante = picante;
    }

    // Metodo propio de PlatoFuerte
     // Los postres no necesitan cocinarse de la misma manera

    cocinar() {
        console.log(` Cocinando ${this.nombre} con ${this.tipoCarne}`);
    }

    // Sobrescribir metodo describir
     // Agrego informacion sobre la carne y si es picante

    describir() {
        return `${super.describir()} - Carne: ${this.tipoCarne} - ${this.picante ? 'Picante' : 'No picante'}`;
    }
}


// DEMOSTRACIÓN
console.log("=== SISTEMA DE COMIDAS ===\n");

// Crear postres
const helado = new Postre("Helado de Vainilla", 3.50, "Italia", true, "frio");
const pastel = new Postre("Pastel de Chocolate", 4.00, "Francia", true, "caliente");

// Crear platos fuertes
const pizza = new PlatoFuerte("Pizza", 12.00, "Italia", "jamon", false);
const taco = new PlatoFuerte("Tacos", 8.50, "Mexico", "res", true);

// Mostrar informacion
console.log("--- POSTRES ---");
console.log(helado.describir());
helado.preparar();
helado.servir();

console.log(pastel.describir());
pastel.servir();

console.log("\n--- PLATOS FUERTES ---");
console.log(pizza.describir());
pizza.preparar();
pizza.cocinar();

console.log(taco.describir());
taco.cocinar();

console.log("\n=== FIN ===");
