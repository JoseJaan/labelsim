"""Faithful port of the 107 measures of Gatto (2021).

Each function transcribes the ``f(a, b, c, d, n)`` version of
``R/functions_measures_binary_data.R`` from the repository
https://github.com/cissagatto/MultiLabelSimilaritiesMeasures, with the same order of
operations and the same precedence as R, including where it diverges from the published
formula. For example, ``a/a+b`` in R equals ``1 + b``, and here as well. The catalog
``catalog/gatto2021.csv`` records each divergence.

R's ``max`` and ``min`` receive scalars in the original code; here they become
``np.maximum`` and ``np.minimum``, which do the same computation element by element.
"""

from numpy import abs, cos, log, log10, maximum, minimum, pi, sqrt

FUNCTIONS = {}


def _gatto(name):
    def register(fn):
        FUNCTIONS[name] = fn
        return fn
    return register


@_gatto("ample.e")
def ample(a, b, c, d, n):
    return abs((a * (c + d)) / (c * (a + b)))


def _anderberg_terms(a, b, c, d):
    delta_1 = maximum(a, b) + maximum(c, d) + maximum(a, c) + maximum(b, d)
    delta_2 = maximum(a + c, b + d) + maximum(a + b, c + d)
    return delta_1, delta_2


@_gatto("anderberg.e")
def anderberg(a, b, c, d, n):
    delta_1, delta_2 = _anderberg_terms(a, b, c, d)
    return (delta_1 - delta_2) / (2 * n)


@_gatto("baroni.urbani.buser.e.1")
def baroni_urbani_buser_1(a, b, c, d, n):
    return (sqrt(abs(a * d)) + a) / (sqrt(abs(a * d)) + a + b + c)


@_gatto("baroni.urbani.buser.e.2")
def baroni_urbani_buser_2(a, b, c, d, n):
    return (a - b - c + sqrt(abs(a * d))) / (a + b + c + sqrt(abs(a * d)))


@_gatto("braun.blanquet.e")
def braun_blanquet(a, b, c, d, n):
    return a / maximum(a + b, a + c)


@_gatto("bray.curtis.e")
def bray_curtis(a, b, c, d, n):
    return (b + c) / ((2 * a) + b + c)


@_gatto("canberra.e")
def canberra(a, b, c, d, n):
    return (b + c) ** (2 / 2)


@_gatto("chord.e")
def chord(a, b, c, d, n):
    d1 = a / sqrt(abs((a + b) * (a + c)))
    return sqrt(abs(2 * (1 - d1)))


@_gatto("cityblock.e")
def cityblock(a, b, c, d, n):
    return b + c


@_gatto("clement.e")
def clement(a, b, c, d, n):
    return a * (c + d) / (a + b) + d * (a + b) / (c + d)


@_gatto("cohen.e")
def cohen(a, b, c, d, n):
    return (2 * ((a * d) - (b * c))) / (((a + b) * (b + d)) + ((a + c) * (c + d)))


@_gatto("cole.e.1")
def cole_1(a, b, c, d, n):
    d2 = ((a * d) - (b * c)) ** 2
    d3 = (a + b) * (a + c) * (b + d) * (c + d)
    return sqrt(abs(d2 - d3))


@_gatto("cole.e.2")
def cole_2(a, b, c, d, n):
    return ((a * d) - (b * c)) / ((a + b) * (b + d))


@_gatto("cole.e.3")
def cole_3(a, b, c, d, n):
    return ((a * d) - (b * c)) / ((a + c) * (c + d))


@_gatto("cosine.e")
def cosine(a, b, c, d, n):
    return a / sqrt(abs((a + b) * (a + c))) ** 2


@_gatto("czekanowski.e")
def czekanowski(a, b, c, d, n):
    return (2 * a) / ((2 * a) + b + c)


@_gatto("dennis.e")
def dennis(a, b, c, d, n):
    return ((a * d) - (b * c)) / sqrt(abs(n * (a + b) * (a + c)))


@_gatto("dibby.e")
def dibby(a, b, c, d, n):
    d1 = (a * d) ** (3 / 4) - (b * c) ** (3 / 4)
    d2 = (a * d) ** (3 / 4) - (b * c) ** (3 / 4)
    return d1 / d2


@_gatto("dice.e.1")
def dice_1(a, b, c, d, n):
    return (2 * a) / ((2 * a) + b + c)


@_gatto("dice.e.2")
def dice_2(a, b, c, d, n):
    return a / a + b


@_gatto("dice.e.3")
def dice_3(a, b, c, d, n):
    return a / a + c


@_gatto("disperson.e")
def disperson(a, b, c, d, n):
    return ((a + d) - (b + c)) / ((a + b + c + d) ** 2)


@_gatto("doolittle.e")
def doolittle(a, b, c, d, n):
    return ((a * d) - (b * c)) ** 2 / ((a + b) * (a + c) * (c + d) * (b + d))


@_gatto("driver.kroeber.e.1")
def driver_kroeber_1(a, b, c, d, n):
    return (a / 2) * ((1 / (a + b)) + (1 / (a + c)))


@_gatto("driver.kroeber.e.2")
def driver_kroeber_2(a, b, c, d, n):
    return a / sqrt(abs((a + b) * (a + c)))


@_gatto("euclidean.e")
def euclidean(a, b, c, d, n):
    return b + c


@_gatto("eyraud.e")
def eyraud(a, b, c, d, n):
    d1 = (n ** 2) * ((n * a) - (a + b) * (a + c))
    d2 = (a + b) * (a + c) * (b + d) * (c + d)
    return d1 / d2


@_gatto("fager.mcgowan.e.1")
def fager_mcgowan_1(a, b, c, d, n):
    d1 = a / sqrt(abs((a + b) * (a + c)))
    d2 = maximum(a + b, a + c) / 2
    return d1 - d2


@_gatto("fager.mcgowan.e.2")
def fager_mcgowan_2(a, b, c, d, n):
    d1 = a / sqrt(abs((a + b) * (a + c)))
    d2 = 1 / (2 * sqrt(abs(maximum(a + b, a + c))))
    return d1 - d2


@_gatto("faith.e")
def faith(a, b, c, d, n):
    return (a + (0.5 * d)) / (a + b + c + d)


@_gatto("fleiss.e")
def fleiss(a, b, c, d, n):
    d1 = ((a * d) - (b * c)) * ((a + b) * (b + d)) + ((a + c) * (c + d))
    d2 = 2 * (a + b) * (a + c) * (c + d) * (b + d)
    return d1 / d2


@_gatto("forbes.e.1")
def forbes_1(a, b, c, d, n):
    return (n * a) / (a + b) * (a + c)


@_gatto("forbes.e.2")
def forbes_2(a, b, c, d, n):
    d1 = (n * a) - (a + b) * (a + c)
    d2 = n * (minimum(a + b, a + c) - ((a + b) * (a + c)))
    return d1 / d2


@_gatto("forbesi.e")
def forbesi(a, b, c, d, n):
    return (n * a) / ((a + b) * (a + c))


@_gatto("fossum.e")
def fossum(a, b, c, d, n):
    return (n * (a - 0.5) ** 2) / (a + b) * (a + c)


@_gatto("gilbert.well.e")
def gilbert_well(a, b, c, d, n):
    return log(a) - log(n) - log((a + b) / n) - log((a + c) / n)


@_gatto("goodman.kruskal.e.1")
def goodman_kruskal_1(a, b, c, d, n):
    z = maximum(a, b) + maximum(c, d) + maximum(a, c) + maximum(b, c)
    w = maximum(a + c, b + d) + maximum(a + b, c + d)
    return (z - w) / ((2 * n) - w)


@_gatto("goodman.kruskal.e.2")
def goodman_kruskal_2(a, b, c, d, n):
    d1 = 2 * minimum(a, d) - b - c
    d2 = 2 * minimum(a, d) + b + c
    return d1 / d2


@_gatto("gower.e")
def gower(a, b, c, d, n):
    return (a + d) / sqrt(abs((a + b) * (a + c) * (b + d) * (c + d)))


@_gatto("gower.legendre.e")
def gower_legendre(a, b, c, d, n):
    return (a + d) / (a + (0.5 * (b + c)) + d)


@_gatto("hamann.e.1")
def hamann_1(a, b, c, d, n):
    return ((a + d) - (b + c)) / (a + b + c + d)


@_gatto("hamann.e.2")
def hamann_2(a, b, c, d, n):
    return (a - b - c + d) / (a + b + c + d)


@_gatto("hamming.e")
def hamming(a, b, c, d, n):
    return b + c


@_gatto("harris.e")
def harris(a, b, c, d, n):
    d1 = (a * (c + d) + (b + d)) / (2 * (a + b + c))
    d2 = (d * (a + b) + (a + c)) / (2 * (b + c + d))
    return d1 + d2


@_gatto("hawkins.dotson.e")
def hawkins_dotson(a, b, c, d, n):
    return (1 / 2) * ((a / a + b + c) + (d / b + c + d))


@_gatto("hellinger.e")
def hellinger(a, b, c, d, n):
    d1 = a / sqrt(abs((a + b) * (a + c)))
    return 2 * sqrt(abs(1 - d1))


@_gatto("inner.product.e")
def inner_product(a, b, c, d, n):
    return a + d


@_gatto("intersection.e")
def intersection(a, b, c, d, n):
    return a + 0.0


@_gatto("jaccard.e")
def jaccard(a, b, c, d, n):
    return a / (a + b + c)


@_gatto("jonhson.e")
def jonhson(a, b, c, d, n):
    return (a / (a + b)) + (a / (a + c))


@_gatto("kent.foster.e.1")
def kent_foster_1(a, b, c, d, n):
    return -(b * c) / (b * (a + b) + c * (a + c) + (b * c))


@_gatto("kent.foster.e.2")
def kent_foster_2(a, b, c, d, n):
    return -(b * c) / (b * (c + d) + c * (b + d) + (b * c))


@_gatto("kuder.richardson.e")
def kuder_richardson(a, b, c, d, n):
    d1 = 4 * ((a * d) - (b * c))
    d2 = ((a + b) * (c + d)) + ((a + c) * (b + d)) + (2 * ((a * d) - (b * c)))
    return d1 / d2


@_gatto("kulczynski.e.1")
def kulczynski_1(a, b, c, d, n):
    return a / (b + c)


@_gatto("kulczynski.e.2")
def kulczynski_2(a, b, c, d, n):
    return ((a / 2) * ((2 * a) + b + c)) / ((a + b) * (a + c))


@_gatto("kulczynski.e.3")
def kulczynski_3(a, b, c, d, n):
    return (1 / 2) * ((a / a + b) + (a / a + c))


@_gatto("kulczynski.e.4")
def kulczynski_4(a, b, c, d, n):
    return a / b + c


@_gatto("lance.williams.e")
def lance_williams(a, b, c, d, n):
    return (b + c) / ((2 * a) + b + c)


@_gatto("loevinger.e")
def loevinger(a, b, c, d, n):
    return ((a * d) - (b * c)) / minimum((a + b) * (b + d), (a + c) * (c + d))


@_gatto("manhattan.e")
def manhattan(a, b, c, d, n):
    return b + c


@_gatto("maxwell.pilliner.e")
def maxwell_pilliner(a, b, c, d, n):
    return (2 * ((a * d) - (b * c))) / ((a + b) * (c + d) + (c + d) * (b + d))


@_gatto("mcconnaughey.e")
def mcconnaughey(a, b, c, d, n):
    return ((a ** 2) - (b - c)) / (a + b) * (a + c)


@_gatto("mean.manhattan.e")
def mean_manhattan(a, b, c, d, n):
    return (b + c) / (a + b + c + d)


@_gatto("michael.e")
def michael(a, b, c, d, n):
    return 4 * ((a * d) - (b * c)) / ((a + d) ** 2) + ((b + c) ** 2)


@_gatto("minowski.e")
def minowski(a, b, c, d, n):
    return (b + c) ** (1 / 1)


@_gatto("mountford.e.1")
def mountford_1(a, b, c, d, n):
    return a / (0.5 * (((a * b) + (a * c)) + (b * c)))


@_gatto("mountford.e.2")
def mountford_2(a, b, c, d, n):
    return (2 * a) / (a * (a + c) + 2 * b * c)


@_gatto("nei.li.e")
def nei_li(a, b, c, d, n):
    return (2 * a) / ((a + b) + (a + c))


@_gatto("ochiai.e.1")
def ochiai_1(a, b, c, d, n):
    return a / sqrt(abs((a + b) * (a + c)))


@_gatto("ochiai.e.2")
def ochiai_2(a, b, c, d, n):
    return (a * d) / sqrt(abs((a + d) * (a + c) * (d + b) * (d + c)))


@_gatto("ochiai.e.3")
def ochiai_3(a, b, c, d, n):
    return (a * d) / sqrt(abs((a + b) * (a + c) * (b + d) * (c + d)))


@_gatto("otsuka.e")
def otsuka(a, b, c, d, n):
    return a / ((a + b) * (a + c)) ** 0.5


@_gatto("pattern.difference.e")
def pattern_difference(a, b, c, d, n):
    return (4 * b * c) / ((a + b + c + d) ** 2)


def _pearson_chi2(a, b, c, d, n):
    d1 = n * (((a * d) - (b * c)) ** 2)
    d2 = (a + b) * (a + c) * (c + d) * (b + d)
    return d1 / d2


@_gatto("pearson.e.1")
def pearson_1(a, b, c, d, n):
    return _pearson_chi2(a, b, c, d, n)


@_gatto("pearson.e.2")
def pearson_2(a, b, c, d, n):
    d3 = _pearson_chi2(a, b, c, d, n)
    return (d3 / n + d3) ** (1 / 2)


@_gatto("pearson.e.3")
def pearson_3(a, b, c, d, n):
    d1 = (a * d) - (b * c)
    d2 = sqrt(abs((a + b) * (a + c) * (b + c) * (c + d)))
    d3 = d1 / d2
    return (d3 / b + d3) ** (1 / 2)


@_gatto("pearson.heron.e.1")
def pearson_heron_1(a, b, c, d, n):
    d1 = (a * d) - (b * c)
    d2 = (a + b) * (a + c) * (b + d) * (c + d)
    return d1 / d2


@_gatto("pearson.heron.e.2")
def pearson_heron_2(a, b, c, d, n):
    d1 = pi * sqrt(abs(b * c))
    d2 = sqrt(abs(a * d)) + sqrt(abs(b * c))
    return cos(d1 / d2)


@_gatto("peirce.e.1")
def peirce_1(a, b, c, d, n):
    return ((a * b) + (b * c)) / ((a * b) + (2 * b * c) + (c * d))


@_gatto("peirce.e.2")
def peirce_2(a, b, c, d, n):
    return ((a * d) - (b * c)) / ((a + b) * (c + d))


@_gatto("peirce.e.3")
def peirce_3(a, b, c, d, n):
    return ((a * d) - (b * c)) / ((a + c) * (b + d))


@_gatto("rogers.tanimoto.e")
def rogers_tanimoto(a, b, c, d, n):
    return (a + d) / (a + (2 * (b + c)) + d)


@_gatto("rogot.goldberd.e")
def rogot_goldberd(a, b, c, d, n):
    d1 = a / (a + b) + (a + c)
    d2 = d / (c + d) + (b + d)
    return d1 + d2


@_gatto("russel.rao.e")
def russel_rao(a, b, c, d, n):
    return a / (a + b + c + d)


@_gatto("scott.e")
def scott(a, b, c, d, n):
    d1 = 4 * a * d - ((b + c) ** 2)
    d2 = ((a + b) + (a + c)) * ((c + d) + (b + d))
    return d1 / d2


@_gatto("shape.difference.e")
def shape_difference(a, b, c, d, n):
    d1 = n * (b + c) - ((b - c) ** 2)
    d2 = (a + b + c + d) ** 2
    return d1 / d2


@_gatto("simpson.e")
def simpson(a, b, c, d, n):
    return a / minimum(a + b, a + c)


@_gatto("size.difference.e")
def size_difference(a, b, c, d, n):
    return (b + c) ** 2 / (a + b + c + d) ** 2


@_gatto("sokal.michener.e")
def sokal_michener(a, b, c, d, n):
    return (a + d) / (a + b + c + d)


@_gatto("sokal.sneath.e.1")
def sokal_sneath_1(a, b, c, d, n):
    return a / (a + (2 * b) + (2 * c))


@_gatto("sokal.sneath.e.2")
def sokal_sneath_2(a, b, c, d, n):
    return 2 * (a + d) / ((2 * a) + b + c + (2 * d))


@_gatto("sokal.sneath.e.3")
def sokal_sneath_3(a, b, c, d, n):
    return (a + d) / (b + c)


@_gatto("sokal.sneath.e.4a")
def sokal_sneath_4a(a, b, c, d, n):
    d1 = 1 / 4
    d2 = (a / a + b) * (a / a + c) * (a / c + d) * (a / b + d)
    return d1 / d2


@_gatto("sokal.sneath.e.4b")
def sokal_sneath_4b(a, b, c, d, n):
    return (a / a + b) * (a / a + c) * (d / b + c) * (d / b + d)


@_gatto("sokal.sneath.e.5a")
def sokal_sneath_5a(a, b, c, d, n):
    return (a * d) / ((a + d) * (a + c) * (b + d) * (c + d)) ** 0.5


@_gatto("sokal.sneath.e.5b")
def sokal_sneath_5b(a, b, c, d, n):
    return (a * d) / sqrt(abs((a + d) * (a + c) * (b + d) * (c + d)))


@_gatto("sorgenfrei.e")
def sorgenfrei(a, b, c, d, n):
    return a ** 2 / ((a + b) * (a + b))


@_gatto("square.euclidean.e")
def square_euclidean(a, b, c, d, n):
    return sqrt(abs((b + c) ** 2))


@_gatto("stiles.e")
def stiles(a, b, c, d, n):
    d1 = n * (abs((a * d) - (n / 2))) ** 2
    d2 = (a + b) * (a + c) * (b + d) * (c + d)
    return log10(d1 / d2)


@_gatto("tanimoto.e")
def tanimoto(a, b, c, d, n):
    return a / ((a + b) + (a + c) - a)


@_gatto("tarantula.e")
def tarantula(a, b, c, d, n):
    return (a * (c + d)) / (c * (a + d))


@_gatto("tarwid.e")
def tarwid(a, b, c, d, n):
    return (n * a - (a + b) * (a + c)) / (n * a + (a + b) * (a + c))


@_gatto("three.w.jaccard.e")
def three_w_jaccard(a, b, c, d, n):
    return (3 * a) / (3 * a + b + c)


@_gatto("vari.e")
def vari(a, b, c, d, n):
    return (b + c) / (4 * (a + b + c + d))


@_gatto("yule.e.1")
def yule_1(a, b, c, d, n):
    d1 = (a * d) - (b * c)
    d2 = (a * d) - (b * c)
    return d1 / d2


@_gatto("yule.e.2")
def yule_2(a, b, c, d, n):
    return (2 * b * c) / ((a * d) + (b * c))


@_gatto("yule.e.3")
def yule_3(a, b, c, d, n):
    d1 = sqrt(abs(a * d)) - sqrt(abs(b * c))
    d2 = sqrt(abs(a * d)) - sqrt(abs(b * c))
    return d1 / d2

