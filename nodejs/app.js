
function hola(nombre, miCallback){
    setTimeout(() => {
        console.log("Hola " + nombre);
        miCallback(nombre);
    }, 1000);
}

const adios = (nombre, miCallback) => {
    setTimeout(() => {
        console.log("Adios " + nombre);
        miCallback();
    }, 1000);
}

function hablar(callback) {
    setTimeout(() => {
        console.log("Bla bla bla ...");
        callback()
    }, 1000);
    
}

function conversation(nombre, veces, callback){
    if (veces > 0){
        hablar(()=>{
            conversation(nombre, --veces, callback);
        });
    } else{
        adios(nombre, callback);
    }
}

// console.log("...Start process....");
// hola("daniel", (nombre) => {
//     conversation(nombre, 5, () => {
//         console.log("...End process...")
//     })
// })

// Promesas

function holaPromisse(nombre){
    return new Promise(function(resolve, reject) {
        setTimeout(() => {
            console.log("Hola " + nombre);
            resolve(nombre);
        }, 1000);
    })
}

const adiosPromisse = (nombre) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("Adios " + nombre);
            resolve();
        }, 1000);
    })

}
function hablarPromisse() {
    return new Promisse((resolve, reject) => {
        setTimeout(() => {
            console.log("Bla bla bla ...");
            reject("HAy un error en hablar");
        }, 1000);
    })

    
}

console.log("iniciando....");
holaPromisse("DAnieeel")
    .then(hablarPromisse)
    .then(adiosPromisse)
    .then((nombre) => {
        console.log("Terminado....");
    })
    .catch(error => {
        console.error("Un error:");
        console.error(error);
    })