# Medidas do labelsim

Gerado por `tools/tabela_medidas.py` a partir de `src/labelsim/catalog/`. Não edite à mão.

Convenção da tabela para o par (i, j), como na Tabela 1 de Choi, Cha e Tappert (2010).

| | j presente | j ausente |
| --- | --- | --- |
| **i presente** | a | c |
| **i ausente** | b | d |

## Variante literature

65 fórmulas distintas. A coluna de nomes de Gatto (2021) lista os nomes do código original que, nesta variante, dão a fórmula da linha.

| id | Medida | Tipo | Fórmula | Referência | Apelidos | Nomes de Gatto (2021) |
| --- | --- | --- | --- | --- | --- | --- |
| `ample` | AMPLE | similaridade | `\|a(c+d)/(c(a+b))\|` | Choi2010, eq. 76 |  | `ample.e` |
| `anderberg` | Anderberg | similaridade | `(s-s')/(2n), com s e s' como em goodman_kruskal` | Choi2010, eq. 70 |  | `anderberg.e` |
| `baroni_urbani_buser_1` | Baroni-Urbani e Buser I | similaridade | `(sqrt(ad)+a)/(sqrt(ad)+a+b+c)` | Choi2010, eq. 71 |  | `baroni.urbani.buser.e.1` |
| `baroni_urbani_buser_2` | Baroni-Urbani e Buser II | similaridade | `(sqrt(ad)+a-(b+c))/(sqrt(ad)+a+b+c)` | Choi2010, eq. 72 |  | `baroni.urbani.buser.e.2` |
| `braun_blanquet` | Braun-Blanquet | similaridade | `a/max(a+b,a+c)` | Choi2010, eq. 46 |  | `braun.blanquet.e` |
| `bray_curtis` | Bray e Curtis | distancia | `(b+c)/(2a+b+c)` | Choi2010, eq. 27 e eq. 28 |  | `bray.curtis.e`, `lance.williams.e` |
| `chord` | Corda | distancia | `sqrt(2(1-a/sqrt((a+b)(a+c))))` | Choi2010, eq. 30 |  | `chord.e` |
| `cole` | Cole | similaridade | `sqrt(2)(ad-bc)/sqrt((ad-bc)^2-(a+b)(a+c)(b+d)(c+d))` | Choi2010, eq. 58 |  | `cole.e.1` |
| `cosine` | Cosseno | similaridade | `a/(sqrt((a+b)(a+c)))^2` | Choi2010, eq. 31 |  | `cosine.e` |
| `dennis` | Dennis | similaridade | `(ad-bc)/sqrt(n(a+b)(a+c))` | Choi2010, eq. 44 |  | `dennis.e` |
| `dice` | Dice | similaridade | `2a/(2a+b+c)` | Choi2010, eq. 2, eq. 3 e eq. 5 |  | `czekanowski.e`, `dice.e.1`, `nei.li.e` |
| `disperson` | Disperson | similaridade | `(ad-bc)/(a+b+c+d)^2` | Choi2010, eq. 66 |  | `disperson.e` |
| `euclidean` | Euclidiana | distancia | `sqrt(b+c)` | Choi2010, eq. 16 |  | `euclidean.e` |
| `eyraud` | Eyraud | similaridade | `n^2(na-(a+b)(a+c))/((a+b)(a+c)(b+d)(c+d))` | Choi2010, eq. 74 |  | `eyraud.e` |
| `fager_mcgowan_1` | Fager e McGowan I | similaridade | `a/sqrt((a+b)(a+c))-max(a+b,a+c)/2` | Choi2010, eq. 47 |  | `fager.mcgowan.e.1` |
| `fager_mcgowan_2` | Fager e McGowan II | similaridade | `a/sqrt((a+b)(a+c))-1/(2 sqrt(max(a+b,a+c)))` | Kim2022, tab. 4 |  | `fager.mcgowan.e.2` |
| `faith` | Faith | similaridade | `(a+0.5d)/(a+b+c+d)` | Choi2010, eq. 10 |  | `faith.e` |
| `forbes_1` | Forbes I | similaridade | `na/((a+b)(a+c))` | Choi2010, eq. 34 |  | `forbes.e.1`, `forbesi.e` |
| `forbes_2` | Forbes II | similaridade | `(na-(a+b)(a+c))/(n min(a+b,a+c)-(a+b)(a+c))` | Choi2010, eq. 48 |  | `forbes.e.2` |
| `fossum` | Fossum | similaridade | `n(a-0.5)^2/((a+b)(a+c))` | Choi2010, eq. 35 |  | `fossum.e` |
| `gilbert_wells` | Gilbert e Wells | similaridade | `log(a)-log(n)-log((a+b)/n)-log((a+c)/n)` | Choi2010, eq. 32 |  | `gilbert.well.e` |
| `goodman_kruskal` | Goodman e Kruskal | similaridade | `(s-s')/(2n-s'), s = max(a,b)+max(c,d)+max(a,c)+max(b,d), s' = max(a+c,b+d)+max(a+b,c+d)` | Choi2010, eq. 69 |  | `goodman.kruskal.e.1` |
| `gower` | Gower | similaridade | `(a+d)/sqrt((a+b)(a+c)(b+d)(c+d))` | Choi2010, eq. 50 |  | `gower.e` |
| `gower_legendre` | Gower e Legendre | similaridade | `(a+d)/(a+0.5(b+c)+d)` | Choi2010, eq. 11 |  | `gower.legendre.e` |
| `hamann` | Hamann | similaridade | `((a+d)-(b+c))/(a+b+c+d)` | Choi2010, eq. 67 |  | `hamann.e.1`, `hamann.e.2` |
| `hamming` | Hamming | distancia | `b+c` | Choi2010, eq. 15, eq. 17, eq. 18, eq. 19, eq. 21 e eq. 22 | `minkowski`, `squared_euclidean` | `canberra.e`, `cityblock.e`, `hamming.e`, `manhattan.e`, `minowski.e`, `square.euclidean.e` |
| `hellinger` | Hellinger | distancia | `2 sqrt(1-a/sqrt((a+b)(a+c)))` | Choi2010, eq. 29 |  | `hellinger.e` |
| `inner_product` | Produto interno | similaridade | `a+d` | Choi2010, eq. 13 |  | `inner.product.e` |
| `intersection` | Interseção | similaridade | `a` | Choi2010, eq. 12 |  | `intersection.e` |
| `jaccard` | Jaccard | similaridade | `a/(a+b+c)` | Choi2010, eq. 1 e eq. 65 |  | `jaccard.e`, `tanimoto.e` |
| `jaccard_3w` | Jaccard com peso 3 | similaridade | `3a/(3a+b+c)` | Choi2010, eq. 4 |  | `three.w.jaccard.e` |
| `johnson` | Johnson | similaridade | `a/(a+b)+a/(a+c)` | Choi2010, eq. 43 |  | `jonhson.e` |
| `kulczynski_1` | Kulczynski I | similaridade | `a/(b+c)` | Choi2010, eq. 64 |  | `kulczynski.e.1`, `kulczynski.e.4` |
| `kulczynski_2` | Kulczynski II | similaridade | `(a/2)(2a+b+c)/((a+b)(a+c))` | Choi2010, eq. 41 e eq. 42 | `kulczynski2`, `driver_kroeber` | `driver.kroeber.e.1`, `kulczynski.e.2`, `kulczynski.e.3` |
| `mcconnaughey` | McConnaughey | similaridade | `(a^2-bc)/((a+b)(a+c))` | Choi2010, eq. 39 |  | `mcconnaughey.e` |
| `mean_manhattan` | Manhattan média | distancia | `(b+c)/(a+b+c+d)` | Choi2010, eq. 20 |  | `mean.manhattan.e` |
| `michael` | Michael | similaridade | `4(ad-bc)/((a+d)^2+(b+c)^2)` | Choi2010, eq. 68 |  | `michael.e` |
| `mountford` | Mountford | similaridade | `a/(0.5(ab+ac)+bc)` | Choi2010, eq. 37; Kim2022, tab. 4 |  | `mountford.e.1`, `mountford.e.2` |
| `nmi` | Informação mútua normalizada | similaridade | `I(i;j)/sqrt(H(i)H(j))` | Strehl2002 |  |  |
| `ochiai_1` | Ochiai I | similaridade | `a/sqrt((a+b)(a+c))` | Choi2010, eq. 33 e eq. 38 | `ochiai` | `ochiai.e.1`, `otsuka.e` |
| `ochiai_2` | Ochiai II | similaridade | `ad/sqrt((a+b)(a+c)(b+d)(c+d))` | Choi2010, eq. 57 e eq. 60 | `sokal_sneath_v`, `sokal_sneath_5` | `ochiai.e.2`, `ochiai.e.3`, `sokal.sneath.e.5a`, `sokal.sneath.e.5b` |
| `pattern_difference` | Diferença de padrão | distancia | `4bc/(a+b+c+d)^2` | Choi2010, eq. 26 |  | `pattern.difference.e` |
| `pearson_1` | Pearson I | similaridade | `n(ad-bc)^2/((a+b)(a+c)(c+d)(b+d))` | Choi2010, eq. 51 |  | `pearson.e.1` |
| `pearson_2` | Pearson II | similaridade | `(chi2/(n+chi2))^(1/2)` | Choi2010, eq. 52 |  | `pearson.e.2` |
| `pearson_3` | Pearson III | similaridade | `(rho/(n+rho))^(1/2)` | Choi2010, eq. 53 |  | `pearson.e.3` |
| `pearson_heron_2` | Pearson e Heron II | similaridade | `cos(pi sqrt(bc)/(sqrt(ad)+sqrt(bc)))` | Choi2010, eq. 55 |  | `pearson.heron.e.2` |
| `peirce` | Peirce | similaridade | `(ab+bc)/(ab+2bc+cd)` | Choi2010, eq. 73 |  | `peirce.e.1` |
| `phi` | Phi (Pearson e Heron I) | similaridade | `(ad-bc)/sqrt((a+b)(a+c)(b+d)(c+d))` | Choi2010, eq. 54 | `pearson_heron_1` | `pearson.heron.e.1` |
| `rogers_tanimoto` | Rogers e Tanimoto | similaridade | `(a+d)/(a+2(b+c)+d)` | Choi2010, eq. 9 |  | `rogers.tanimoto.e` |
| `russell_rao` | Russell e Rao | similaridade | `a/(a+b+c+d)` | Choi2010, eq. 14 | `russel_rao` | `russel.rao.e` |
| `shape_difference` | Diferença de forma | distancia | `(n(b+c)-(b-c)^2)/(a+b+c+d)^2` | Choi2010, eq. 25 |  | `shape.difference.e` |
| `simpson` | Simpson | similaridade | `a/min(a+b,a+c)` | Choi2010, eq. 45 |  | `simpson.e` |
| `size_difference` | Diferença de tamanho | distancia | `(b+c)^2/(a+b+c+d)^2` | Choi2010, eq. 24 |  | `size.difference.e` |
| `sokal_michener` | Sokal e Michener | similaridade | `(a+d)/(a+b+c+d)` | Choi2010, eq. 7 |  | `sokal.michener.e` |
| `sokal_sneath_1` | Sokal e Sneath I | similaridade | `a/(a+2b+2c)` | Choi2010, eq. 6 |  | `sokal.sneath.e.1` |
| `sokal_sneath_2` | Sokal e Sneath II | similaridade | `2(a+d)/(2a+b+c+2d)` | Choi2010, eq. 8 |  | `sokal.sneath.e.2` |
| `sokal_sneath_3` | Sokal e Sneath III | similaridade | `(a+d)/(b+c)` | Choi2010, eq. 56 |  | `sokal.sneath.e.3` |
| `sorgenfrei` | Sorgenfrei | similaridade | `a^2/((a+b)(a+c))` | Choi2010, eq. 36 |  | `sorgenfrei.e` |
| `stiles` | Stiles | similaridade | `log10(n(\|ad-bc\|-n/2)^2/((a+b)(a+c)(b+d)(c+d)))` | Choi2010, eq. 59 |  | `stiles.e` |
| `tarantula` | Tarantula | similaridade | `a(c+d)/(c(a+b))` | Choi2010, eq. 75 |  | `tarantula.e` |
| `tarwid` | Tarwid | similaridade | `(na-(a+b)(a+c))/(na+(a+b)(a+c))` | Choi2010, eq. 40 |  | `tarwid.e` |
| `vari` | Vari | distancia | `(b+c)/(4(a+b+c+d))` | Choi2010, eq. 23 |  | `vari.e` |
| `yule_q` | Q de Yule | similaridade | `(ad-bc)/(ad+bc)` | Choi2010, eq. 61 |  | `yule.e.1` |
| `yule_q_distance` | Distância Q de Yule | distancia | `2bc/(ad+bc)` | Choi2010, eq. 62 |  | `yule.e.2` |
| `yule_w` | W de Yule | similaridade | `(sqrt(ad)-sqrt(bc))/(sqrt(ad)+sqrt(bc))` | Choi2010, eq. 63 |  | `yule.e.3` |

## Variante gatto2021

Os 107 nomes de `getNamesListFunctions()`, transcritos do código R original com a mesma precedência de operadores.

| Situação | Nomes | Significado |
| --- | --- | --- |
| `correta` | 59 | Igual à fórmula publicada. |
| `erro_precedencia` | 10 | A precedência de operadores do R muda a conta. |
| `termo_trocado` | 9 | Um termo da fórmula foi trocado por outro. |
| `formula_divergente` | 3 | A expressão difere da publicada de outra forma. |
| `constante` | 2 | Numerador e denominador iguais; vale 1 ou NaN. |
| `fonte_pendente` | 24 | Sem fórmula conferida em fonte disponível; só existe a variante gatto2021. |

| Nome original | id | Situação | Fórmula no código | Fórmula da literatura | Nota |
| --- | --- | --- | --- | --- | --- |
| `ample.e` | `ample` | correta | `abs(a*(c+d)/(c*(a+b)))` | `ample` |  |
| `anderberg.e` | `anderberg` | correta | `(max(a;b)+max(c;d)+max(a;c)+max(b;d)-max(a+c;b+d)-max(a+b;c+d))/(2*n)` | `anderberg` |  |
| `baroni.urbani.buser.e.1` | `baroni_urbani_buser_1` | correta | `(sqrt(abs(a*d))+a)/(sqrt(abs(a*d))+a+b+c)` | `baroni_urbani_buser_1` |  |
| `baroni.urbani.buser.e.2` | `baroni_urbani_buser_2` | correta | `(a-b-c+sqrt(abs(a*d)))/(a+b+c+sqrt(abs(a*d)))` | `baroni_urbani_buser_2` |  |
| `braun.blanquet.e` | `braun_blanquet` | correta | `a/max(a+b;a+c)` | `braun_blanquet` |  |
| `bray.curtis.e` | `bray_curtis` | correta | `(b+c)/(2*a+b+c)` | `bray_curtis` |  |
| `canberra.e` | `canberra` | correta | `(b+c)^(2/2)` | `hamming` |  |
| `chord.e` | `chord` | correta | `sqrt(abs(2*(1-a/sqrt(abs((a+b)*(a+c))))))` | `chord` |  |
| `cityblock.e` | `cityblock` | correta | `b+c` | `hamming` |  |
| `clement.e` | `clement` | fonte_pendente | `a*(c+d)/(a+b)+d*(a+b)/(c+d)` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `cohen.e` | `cohen` | fonte_pendente | `2*(a*d-b*c)/((a+b)*(b+d)+(a+c)*(c+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `cole.e.1` | `cole_1` | formula_divergente | `sqrt(abs((a*d-b*c)^2-(a+b)*(a+c)*(b+d)*(c+d)))` | `cole` | Calcula o numerador sqrt(2)*(a*d-b*c) e não o usa; devolve só a raiz do denominador, com valor absoluto. |
| `cole.e.2` | `cole_2` | fonte_pendente | `(a*d-b*c)/((a+b)*(b+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `cole.e.3` | `cole_3` | fonte_pendente | `(a*d-b*c)/((a+c)*(c+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `cosine.e` | `cosine` | correta | `a/sqrt(abs((a+b)*(a+c)))^2` | `cosine` |  |
| `czekanowski.e` | `czekanowski` | correta | `2*a/(2*a+b+c)` | `dice` |  |
| `dennis.e` | `dennis` | correta | `(a*d-b*c)/sqrt(abs(n*(a+b)*(a+c)))` | `dennis` |  |
| `dibby.e` | `dibby` | fonte_pendente | `((a*d)^(3/4)-(b*c)^(3/4))/((a*d)^(3/4)-(b*c)^(3/4))` |  | Fórmula ausente de Choi (2010) e Kim (2022). Numerador e denominador são a mesma expressão, então vale 1, ou NaN quando a expressão é zero. O nome no código original está grafado dibby; a versão em lista se chama digby.e.1. |
| `dice.e.1` | `dice_1` | correta | `2*a/(2*a+b+c)` | `dice` |  |
| `dice.e.2` | `dice_2` | fonte_pendente | `a/a+b` |  | Fórmula ausente de Choi (2010) e Kim (2022). Pela precedência do R, a/a+b vale 1+b. |
| `dice.e.3` | `dice_3` | fonte_pendente | `a/a+c` |  | Fórmula ausente de Choi (2010) e Kim (2022). Pela precedência do R, a/a+c vale 1+c. |
| `disperson.e` | `disperson` | termo_trocado | `((a+d)-(b+c))/(a+b+c+d)^2` | `disperson` | O numerador usa (a+d)-(b+c) no lugar de ad-bc. |
| `doolittle.e` | `doolittle` | fonte_pendente | `(a*d-b*c)^2/((a+b)*(a+c)*(c+d)*(b+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `driver.kroeber.e.1` | `driver_kroeber_1` | correta | `(a/2)*(1/(a+b)+1/(a+c))` | `kulczynski_2` |  |
| `driver.kroeber.e.2` | `driver_kroeber_2` | fonte_pendente | `a/sqrt(abs((a+b)*(a+c)))` |  | A expressão é a de Ochiai I, mas nenhuma fonte disponível atribui essa forma a Driver e Kroeber. |
| `euclidean.e` | `euclidean` | formula_divergente | `b+c` | `euclidean` | Falta a raiz quadrada de sqrt(b+c). |
| `eyraud.e` | `eyraud` | correta | `n^2*(n*a-(a+b)*(a+c))/((a+b)*(a+c)*(b+d)*(c+d))` | `eyraud` |  |
| `fager.mcgowan.e.1` | `fager_mcgowan_1` | correta | `a/sqrt(abs((a+b)*(a+c)))-max(a+b;a+c)/2` | `fager_mcgowan_1` |  |
| `fager.mcgowan.e.2` | `fager_mcgowan_2` | correta | `a/sqrt(abs((a+b)*(a+c)))-1/(2*sqrt(abs(max(a+b;a+c))))` | `fager_mcgowan_2` |  |
| `faith.e` | `faith` | correta | `(a+0.5*d)/(a+b+c+d)` | `faith` |  |
| `fleiss.e` | `fleiss` | fonte_pendente | `((a*d-b*c)*((a+b)*(b+d))+((a+c)*(c+d)))/(2*(a+b)*(a+c)*(c+d)*(b+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `forbes.e.1` | `forbes_1` | erro_precedencia | `(n*a)/(a+b)*(a+c)` | `forbes_1` | Pela precedência do R, multiplica por (a+c) em vez de dividir. |
| `forbes.e.2` | `forbes_2` | erro_precedencia | `(n*a-(a+b)*(a+c))/(n*(min(a+b;a+c)-(a+b)*(a+c)))` | `forbes_2` | O parêntese multiplica n também pelo produto das marginais no denominador. |
| `forbesi.e` | `forbesi` | correta | `(n*a)/((a+b)*(a+c))` | `forbes_1` |  |
| `fossum.e` | `fossum` | erro_precedencia | `(n*(a-0.5)^2)/(a+b)*(a+c)` | `fossum` | Pela precedência do R, multiplica por (a+c) em vez de dividir. |
| `gilbert.well.e` | `gilbert_well` | correta | `log(a)-log(n)-log((a+b)/n)-log((a+c)/n)` | `gilbert_wells` |  |
| `goodman.kruskal.e.1` | `goodman_kruskal_1` | termo_trocado | `(s-s')/(2*n-s'), s = max(a;b)+max(c;d)+max(a;c)+max(b;c), s' = max(a+c;b+d)+max(a+b;c+d)` | `goodman_kruskal` | O último termo de s usa max(b;c) no lugar de max(b;d). |
| `goodman.kruskal.e.2` | `goodman_kruskal_2` | fonte_pendente | `(2*min(a;d)-b-c)/(2*min(a;d)+b+c)` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `gower.e` | `gower` | correta | `(a+d)/sqrt(abs((a+b)*(a+c)*(b+d)*(c+d)))` | `gower` |  |
| `gower.legendre.e` | `gower_legendre` | correta | `(a+d)/(a+0.5*(b+c)+d)` | `gower_legendre` |  |
| `hamann.e.1` | `hamann_1` | correta | `((a+d)-(b+c))/(a+b+c+d)` | `hamann` |  |
| `hamann.e.2` | `hamann_2` | correta | `(a-b-c+d)/(a+b+c+d)` | `hamann` |  |
| `hamming.e` | `hamming` | correta | `b+c` | `hamming` |  |
| `harris.e` | `harris` | fonte_pendente | `(a*(c+d)+(b+d))/(2*(a+b+c))+(d*(a+b)+(a+c))/(2*(b+c+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `hawkins.dotson.e` | `hawkins_dotson` | fonte_pendente | `(1/2)*((a/a+b+c)+(d/b+c+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). Pela precedência do R, a/a+b+c vale 1+b+c e d/b+c+d vale d/b+c+d. |
| `hellinger.e` | `hellinger` | correta | `2*sqrt(abs(1-a/sqrt(abs((a+b)*(a+c)))))` | `hellinger` |  |
| `inner.product.e` | `inner_product` | correta | `a+d` | `inner_product` |  |
| `intersection.e` | `intersection` | correta | `a` | `intersection` |  |
| `jaccard.e` | `jaccard` | correta | `a/(a+b+c)` | `jaccard` |  |
| `jonhson.e` | `jonhson` | correta | `a/(a+b)+a/(a+c)` | `johnson` | O nome no código original está grafado jonhson. |
| `kent.foster.e.1` | `kent_foster_1` | fonte_pendente | `-(b*c)/(b*(a+b)+c*(a+c)+b*c)` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `kent.foster.e.2` | `kent_foster_2` | fonte_pendente | `-(b*c)/(b*(c+d)+c*(b+d)+b*c)` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `kuder.richardson.e` | `kuder_richardson` | fonte_pendente | `4*(a*d-b*c)/((a+b)*(c+d)+(a+c)*(b+d)+2*(a*d-b*c))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `kulczynski.e.1` | `kulczynski_1` | correta | `a/(b+c)` | `kulczynski_1` |  |
| `kulczynski.e.2` | `kulczynski_2` | correta | `(a/2)*(2*a+b+c)/((a+b)*(a+c))` | `kulczynski_2` |  |
| `kulczynski.e.3` | `kulczynski_3` | erro_precedencia | `(1/2)*((a/a+b)+(a/a+c))` | `kulczynski_2` | Pela precedência do R, a/a+b vale 1+b. A forma pretendida, (1/2)(a/(a+b)+a/(a+c)), é a eq. 42 de Choi (2010). |
| `kulczynski.e.4` | `kulczynski_4` | erro_precedencia | `a/b+c` | `kulczynski_1` | Pela precedência do R, a/b+c soma c a a/b. A forma pretendida, a/(b+c), é a eq. 64 de Choi (2010). |
| `lance.williams.e` | `lance_williams` | correta | `(b+c)/(2*a+b+c)` | `bray_curtis` |  |
| `loevinger.e` | `loevinger` | fonte_pendente | `(a*d-b*c)/min((a+b)*(b+d);(a+c)*(c+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `manhattan.e` | `manhattan` | correta | `b+c` | `hamming` |  |
| `maxwell.pilliner.e` | `maxwell_pilliner` | fonte_pendente | `2*(a*d-b*c)/((a+b)*(c+d)+(c+d)*(b+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `mcconnaughey.e` | `mcconnaughey` | erro_precedencia | `(a^2-(b-c))/(a+b)*(a+c)` | `mcconnaughey` | Pela precedência do R, multiplica por (a+c) em vez de dividir; o numerador usa b-c no lugar de bc. |
| `mean.manhattan.e` | `mean_manhattan` | correta | `(b+c)/(a+b+c+d)` | `mean_manhattan` |  |
| `michael.e` | `michael` | erro_precedencia | `4*(a*d-b*c)/((a+d)^2)+((b+c)^2)` | `michael` | Pela precedência do R, (b+c)^2 é somado ao quociente em vez de entrar no denominador. |
| `minowski.e` | `minowski` | correta | `(b+c)^(1/1)` | `hamming` | O nome no código original está grafado minowski. |
| `mountford.e.1` | `mountford_1` | erro_precedencia | `a/(0.5*((a*b+a*c)+b*c))` | `mountford` | O parêntese multiplica bc por 0.5. |
| `mountford.e.2` | `mountford_2` | termo_trocado | `2*a/(a*(a+c)+2*b*c)` | `mountford` | O denominador usa a(a+c) no lugar de a(b+c). |
| `nei.li.e` | `nei_li` | correta | `2*a/((a+b)+(a+c))` | `dice` |  |
| `ochiai.e.1` | `ochiai_1` | correta | `a/sqrt(abs((a+b)*(a+c)))` | `ochiai_1` |  |
| `ochiai.e.2` | `ochiai_2` | termo_trocado | `a*d/sqrt(abs((a+d)*(a+c)*(d+b)*(d+c)))` | `ochiai_2` | O denominador usa (a+d) no lugar de (a+b). |
| `ochiai.e.3` | `ochiai_3` | correta | `a*d/sqrt(abs((a+b)*(a+c)*(b+d)*(c+d)))` | `ochiai_2` |  |
| `otsuka.e` | `otsuka` | correta | `a/((a+b)*(a+c))^0.5` | `ochiai_1` |  |
| `pattern.difference.e` | `pattern_difference` | correta | `4*b*c/(a+b+c+d)^2` | `pattern_difference` |  |
| `pearson.e.1` | `pearson_1` | correta | `n*(a*d-b*c)^2/((a+b)*(a+c)*(c+d)*(b+d))` | `pearson_1` |  |
| `pearson.e.2` | `pearson_2` | erro_precedencia | `(chi2/n+chi2)^(1/2)` | `pearson_2` | Pela precedência do R, chi2/n+chi2 soma chi2 a chi2/n em vez de dividir por n+chi2. |
| `pearson.e.3` | `pearson_3` | erro_precedencia | `(rho/b+rho)^(1/2) com rho = (a*d-b*c)/sqrt(abs((a+b)*(a+c)*(b+c)*(c+d)))` | `pearson_3` | Pela precedência do R, rho/b+rho soma rho a rho/b; além disso, divide por b no lugar de n, e rho usa (b+c) no lugar de (b+d). |
| `pearson.heron.e.1` | `pearson_heron_1` | formula_divergente | `(a*d-b*c)/((a+b)*(a+c)*(b+d)*(c+d))` | `phi` | Calcula a raiz do produto das marginais e não a usa; divide pelo produto sem raiz. |
| `pearson.heron.e.2` | `pearson_heron_2` | correta | `cos(pi*sqrt(abs(b*c))/(sqrt(abs(a*d))+sqrt(abs(b*c))))` | `pearson_heron_2` |  |
| `peirce.e.1` | `peirce_1` | correta | `(a*b+b*c)/(a*b+2*b*c+c*d)` | `peirce` |  |
| `peirce.e.2` | `peirce_2` | fonte_pendente | `(a*d-b*c)/((a+b)*(c+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `peirce.e.3` | `peirce_3` | fonte_pendente | `(a*d-b*c)/((a+c)*(b+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `rogers.tanimoto.e` | `rogers_tanimoto` | correta | `(a+d)/(a+2*(b+c)+d)` | `rogers_tanimoto` |  |
| `rogot.goldberd.e` | `rogot_goldberd` | fonte_pendente | `(a/(a+b)+(a+c))+(d/(c+d)+(b+d))` |  | Fórmula ausente de Choi (2010) e Kim (2022). Pela precedência do R, (a+c) e (b+d) são somados em vez de entrar nos denominadores. |
| `russel.rao.e` | `russel_rao` | correta | `a/(a+b+c+d)` | `russell_rao` |  |
| `scott.e` | `scott` | fonte_pendente | `(4*a*d-(b+c)^2)/(((a+b)+(a+c))*((c+d)+(b+d)))` |  | Fórmula ausente de Choi (2010) e Kim (2022). |
| `shape.difference.e` | `shape_difference` | correta | `(n*(b+c)-(b-c)^2)/(a+b+c+d)^2` | `shape_difference` |  |
| `simpson.e` | `simpson` | correta | `a/min(a+b;a+c)` | `simpson` |  |
| `size.difference.e` | `size_difference` | correta | `(b+c)^2/(a+b+c+d)^2` | `size_difference` |  |
| `sokal.michener.e` | `sokal_michener` | correta | `(a+d)/(a+b+c+d)` | `sokal_michener` |  |
| `sokal.sneath.e.1` | `sokal_sneath_1` | correta | `a/(a+2*b+2*c)` | `sokal_sneath_1` |  |
| `sokal.sneath.e.2` | `sokal_sneath_2` | correta | `2*(a+d)/(2*a+b+c+2*d)` | `sokal_sneath_2` |  |
| `sokal.sneath.e.3` | `sokal_sneath_3` | correta | `(a+d)/(b+c)` | `sokal_sneath_3` |  |
| `sokal.sneath.e.4a` | `sokal_sneath_4a` | fonte_pendente | `(1/4)/((a/a+b)*(a/a+c)*(a/c+d)*(a/b+d))` |  | Corresponde à Sokal e Sneath IV, mas a eq. 49 de Choi (2010) repete o termo d/(b+d), e a fonte original não foi consultada. Pela precedência do R, a/a+b vale 1+b. |
| `sokal.sneath.e.4b` | `sokal_sneath_4b` | fonte_pendente | `(a/a+b)*(a/a+c)*(d/b+c)*(d/b+d)` |  | Corresponde à Sokal e Sneath IV, mas a eq. 49 de Choi (2010) repete o termo d/(b+d), e a fonte original não foi consultada. Pela precedência do R, a/a+b vale 1+b. |
| `sokal.sneath.e.5a` | `sokal_sneath_5a` | termo_trocado | `a*d/((a+d)*(a+c)*(b+d)*(c+d))^0.5` | `ochiai_2` | O denominador usa (a+d) no lugar de (a+b). |
| `sokal.sneath.e.5b` | `sokal_sneath_5b` | termo_trocado | `a*d/sqrt(abs((a+d)*(a+c)*(b+d)*(c+d)))` | `ochiai_2` | O denominador usa (a+d) no lugar de (a+b). |
| `sorgenfrei.e` | `sorgenfrei` | termo_trocado | `a^2/((a+b)*(a+b))` | `sorgenfrei` | O denominador usa (a+b)(a+b) no lugar de (a+b)(a+c). |
| `square.euclidean.e` | `square_euclidean` | correta | `sqrt(abs((b+c)^2))` | `hamming` |  |
| `stiles.e` | `stiles` | termo_trocado | `log10(n*abs(a*d-n/2)^2/((a+b)*(a+c)*(b+d)*(c+d)))` | `stiles` | O numerador usa \|ad-n/2\| no lugar de \|ad-bc\|-n/2. |
| `tanimoto.e` | `tanimoto` | correta | `a/((a+b)+(a+c)-a)` | `jaccard` |  |
| `tarantula.e` | `tarantula` | termo_trocado | `a*(c+d)/(c*(a+d))` | `tarantula` | O denominador usa c(a+d) no lugar de c(a+b). |
| `tarwid.e` | `tarwid` | correta | `(n*a-(a+b)*(a+c))/(n*a+(a+b)*(a+c))` | `tarwid` |  |
| `three.w.jaccard.e` | `three_w_jaccard` | correta | `3*a/(3*a+b+c)` | `jaccard_3w` |  |
| `vari.e` | `vari` | correta | `(b+c)/(4*(a+b+c+d))` | `vari` |  |
| `yule.e.1` | `yule_1` | constante | `(a*d-b*c)/(a*d-b*c)` | `yule_q` | Numerador e denominador são a mesma expressão, então vale 1, ou NaN quando ad = bc. A forma pretendida é a eq. 61 de Choi (2010). |
| `yule.e.2` | `yule_2` | correta | `2*b*c/(a*d+b*c)` | `yule_q_distance` |  |
| `yule.e.3` | `yule_3` | constante | `(sqrt(abs(a*d))-sqrt(abs(b*c)))/(sqrt(abs(a*d))-sqrt(abs(b*c)))` | `yule_w` | Numerador e denominador são a mesma expressão, então vale 1, ou NaN quando ad = bc. A forma pretendida é a eq. 63 de Choi (2010). |
