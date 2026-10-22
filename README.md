# memory-taint-paths

## Français

Propager révocations et contaminations dans les dérivations de mémoires.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m memory_taint_paths examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Calcule le plus petit point fixe de support propre (AND dans une dérivation, OR entre alternatives), puis les chemins de contamination depuis les révocations. Une autre source propre n’efface pas le besoin de revoir un texte déjà dérivé d’une source révoquée.

### Limites

Graphe fourni, 1 000 nœuds maximum ; aucune inspection de stockage, suppression réelle ou preuve d’effacement. Les cycles sans source ne se justifient pas eux-mêmes.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Propagate revocation and contamination through memory derivations.

Synthetic data; no network access or secret required.

```sh
python -m memory_taint_paths examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Computes least-fixed-point clean support (AND within a derivation, OR between alternatives), then taint paths from revocations. An alternative clean source does not erase the need to review text already derived from a revoked source.

### Limits

Supplied graph, at most 1,000 nodes; no storage inspection, actual deletion or erasure proof. Source-free cycles cannot justify themselves.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Propagar revocación y contaminación en derivaciones de memorias.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m memory_taint_paths examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Calcula soporte limpio por mínimo punto fijo (AND dentro de derivación, OR entre alternativas) y caminos de contaminación desde revocaciones. Una fuente limpia alternativa no elimina la revisión de texto derivado de una fuente revocada.

### Límites

Grafo proporcionado, máximo 1.000 nodos; sin inspección de almacenamiento, borrado real ni prueba de eliminación. Ciclos sin fuente no se justifican solos.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/gbesse/agent-memory-revocation
- https://github.com/gbesse/brain-breakers
