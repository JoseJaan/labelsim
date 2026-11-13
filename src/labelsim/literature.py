"""Formulas of the measures as published.

One function per distinct formula. Names that yield the same formula, such as Tanimoto
and Jaccard, point to the same function through the catalog ``catalog/medidas.csv``,
which also stores the reference of each one.

The table convention is that of Table 1 of Choi, Cha and Tappert (2010), for the pair
(i, j)
    a  i present and j present
    b  i absent and j present
    c  i present and j absent
    d  i absent and j absent
with n = a + b + c + d. The formulas are transcribed as printed in the source, even when
the printed form has unexpected consequences, recorded in the ``nota`` column of the
catalog.
"""

import numpy as np

FUNCTIONS = {}


def _measure(measure_id):
    def register(fn):
        FUNCTIONS[measure_id] = fn
        return fn
    return register


@_measure("jaccard")
def jaccard(a, b, c, d, n):
    return a / (a + b + c)


@_measure("dice")
def dice(a, b, c, d, n):
    return 2 * a / (2 * a + b + c)


@_measure("jaccard_3w")
def jaccard_3w(a, b, c, d, n):
    return 3 * a / (3 * a + b + c)


@_measure("sokal_sneath_1")
def sokal_sneath_1(a, b, c, d, n):
    return a / (a + 2 * b + 2 * c)


@_measure("sokal_michener")
def sokal_michener(a, b, c, d, n):
    return (a + d) / (a + b + c + d)


@_measure("sokal_sneath_2")
def sokal_sneath_2(a, b, c, d, n):
    return 2 * (a + d) / (2 * a + b + c + 2 * d)


@_measure("rogers_tanimoto")
def rogers_tanimoto(a, b, c, d, n):
    return (a + d) / (a + 2 * (b + c) + d)


@_measure("faith")
def faith(a, b, c, d, n):
    return (a + 0.5 * d) / (a + b + c + d)


@_measure("gower_legendre")
def gower_legendre(a, b, c, d, n):
    return (a + d) / (a + 0.5 * (b + c) + d)


@_measure("intersection")
def intersection(a, b, c, d, n):
    return a + 0.0


@_measure("inner_product")
def inner_product(a, b, c, d, n):
    return a + d


@_measure("russell_rao")
def russell_rao(a, b, c, d, n):
    return a / (a + b + c + d)


@_measure("hamming")
def hamming(a, b, c, d, n):
    return b + c


@_measure("euclidean")
def euclidean(a, b, c, d, n):
    return np.sqrt(b + c)


@_measure("mean_manhattan")
def mean_manhattan(a, b, c, d, n):
    return (b + c) / (a + b + c + d)


@_measure("vari")
def vari(a, b, c, d, n):
    return (b + c) / (4 * (a + b + c + d))


@_measure("size_difference")
def size_difference(a, b, c, d, n):
    return (b + c) ** 2 / (a + b + c + d) ** 2


@_measure("shape_difference")
def shape_difference(a, b, c, d, n):
    return (n * (b + c) - (b - c) ** 2) / (a + b + c + d) ** 2


@_measure("pattern_difference")
def pattern_difference(a, b, c, d, n):
    return 4 * b * c / (a + b + c + d) ** 2


@_measure("bray_curtis")
def bray_curtis(a, b, c, d, n):
    return (b + c) / (2 * a + b + c)


@_measure("hellinger")
def hellinger(a, b, c, d, n):
    return 2 * np.sqrt(1 - a / np.sqrt((a + b) * (a + c)))


@_measure("chord")
def chord(a, b, c, d, n):
    return np.sqrt(2 * (1 - a / np.sqrt((a + b) * (a + c))))


@_measure("cosine")
def cosine(a, b, c, d, n):
    return a / np.sqrt((a + b) * (a + c)) ** 2


@_measure("gilbert_wells")
def gilbert_wells(a, b, c, d, n):
    return np.log(a) - np.log(n) - np.log((a + b) / n) - np.log((a + c) / n)


@_measure("ochiai_1")
def ochiai_1(a, b, c, d, n):
    return a / np.sqrt((a + b) * (a + c))


@_measure("forbes_1")
def forbes_1(a, b, c, d, n):
    return n * a / ((a + b) * (a + c))


@_measure("fossum")
def fossum(a, b, c, d, n):
    return n * (a - 0.5) ** 2 / ((a + b) * (a + c))


@_measure("sorgenfrei")
def sorgenfrei(a, b, c, d, n):
    return a ** 2 / ((a + b) * (a + c))


@_measure("mountford")
def mountford(a, b, c, d, n):
    return a / (0.5 * (a * b + a * c) + b * c)


@_measure("mcconnaughey")
def mcconnaughey(a, b, c, d, n):
    return (a ** 2 - b * c) / ((a + b) * (a + c))


@_measure("tarwid")
def tarwid(a, b, c, d, n):
    return (n * a - (a + b) * (a + c)) / (n * a + (a + b) * (a + c))


@_measure("kulczynski_2")
def kulczynski_2(a, b, c, d, n):
    return (a / 2) * (2 * a + b + c) / ((a + b) * (a + c))


@_measure("johnson")
def johnson(a, b, c, d, n):
    return a / (a + b) + a / (a + c)


@_measure("dennis")
def dennis(a, b, c, d, n):
    return (a * d - b * c) / np.sqrt(n * (a + b) * (a + c))


@_measure("simpson")
def simpson(a, b, c, d, n):
    return a / np.minimum(a + b, a + c)


@_measure("braun_blanquet")
def braun_blanquet(a, b, c, d, n):
    return a / np.maximum(a + b, a + c)


@_measure("fager_mcgowan_1")
def fager_mcgowan_1(a, b, c, d, n):
    return a / np.sqrt((a + b) * (a + c)) - np.maximum(a + b, a + c) / 2


@_measure("fager_mcgowan_2")
def fager_mcgowan_2(a, b, c, d, n):
    return a / np.sqrt((a + b) * (a + c)) - 1 / (2 * np.sqrt(np.maximum(a + b, a + c)))


@_measure("forbes_2")
def forbes_2(a, b, c, d, n):
    product = (a + b) * (a + c)
    return (n * a - product) / (n * np.minimum(a + b, a + c) - product)


def _marginal_product(a, b, c, d):
    return (a + b) * (a + c) * (b + d) * (c + d)


@_measure("gower")
def gower(a, b, c, d, n):
    return (a + d) / np.sqrt(_marginal_product(a, b, c, d))


@_measure("pearson_1")
def pearson_1(a, b, c, d, n):
    return n * (a * d - b * c) ** 2 / ((a + b) * (a + c) * (c + d) * (b + d))


@_measure("pearson_2")
def pearson_2(a, b, c, d, n):
    chi2 = pearson_1(a, b, c, d, n)
    return np.power(chi2 / (n + chi2), 0.5)


@_measure("pearson_3")
def pearson_3(a, b, c, d, n):
    rho = phi(a, b, c, d, n)
    return np.power(rho / (n + rho), 0.5)


@_measure("phi")
def phi(a, b, c, d, n):
    return (a * d - b * c) / np.sqrt(_marginal_product(a, b, c, d))


@_measure("pearson_heron_2")
def pearson_heron_2(a, b, c, d, n):
    return np.cos(np.pi * np.sqrt(b * c) / (np.sqrt(a * d) + np.sqrt(b * c)))


@_measure("sokal_sneath_3")
def sokal_sneath_3(a, b, c, d, n):
    return (a + d) / (b + c)


@_measure("ochiai_2")
def ochiai_2(a, b, c, d, n):
    return a * d / np.sqrt(_marginal_product(a, b, c, d))


@_measure("cole")
def cole(a, b, c, d, n):
    association = a * d - b * c
    return np.sqrt(2) * association / np.sqrt(association ** 2 - _marginal_product(a, b, c, d))


@_measure("stiles")
def stiles(a, b, c, d, n):
    return np.log10(n * (np.abs(a * d - b * c) - n / 2) ** 2 / _marginal_product(a, b, c, d))


@_measure("yule_q")
def yule_q(a, b, c, d, n):
    return (a * d - b * c) / (a * d + b * c)


@_measure("yule_q_distance")
def yule_q_distance(a, b, c, d, n):
    return 2 * b * c / (a * d + b * c)


@_measure("yule_w")
def yule_w(a, b, c, d, n):
    return (np.sqrt(a * d) - np.sqrt(b * c)) / (np.sqrt(a * d) + np.sqrt(b * c))


@_measure("kulczynski_1")
def kulczynski_1(a, b, c, d, n):
    return a / (b + c)


@_measure("disperson")
def disperson(a, b, c, d, n):
    return (a * d - b * c) / (a + b + c + d) ** 2


@_measure("hamann")
def hamann(a, b, c, d, n):
    return ((a + d) - (b + c)) / (a + b + c + d)


@_measure("michael")
def michael(a, b, c, d, n):
    return 4 * (a * d - b * c) / ((a + d) ** 2 + (b + c) ** 2)


def _sigmas(a, b, c, d):
    sigma = np.maximum(a, b) + np.maximum(c, d) + np.maximum(a, c) + np.maximum(b, d)
    sigma_prime = np.maximum(a + c, b + d) + np.maximum(a + b, c + d)
    return sigma, sigma_prime


@_measure("goodman_kruskal")
def goodman_kruskal(a, b, c, d, n):
    sigma, sigma_prime = _sigmas(a, b, c, d)
    return (sigma - sigma_prime) / (2 * n - sigma_prime)


@_measure("anderberg")
def anderberg(a, b, c, d, n):
    sigma, sigma_prime = _sigmas(a, b, c, d)
    return (sigma - sigma_prime) / (2 * n)


@_measure("baroni_urbani_buser_1")
def baroni_urbani_buser_1(a, b, c, d, n):
    root = np.sqrt(a * d)
    return (root + a) / (root + a + b + c)


@_measure("baroni_urbani_buser_2")
def baroni_urbani_buser_2(a, b, c, d, n):
    root = np.sqrt(a * d)
    return (root + a - (b + c)) / (root + a + b + c)


@_measure("peirce")
def peirce(a, b, c, d, n):
    return (a * b + b * c) / (a * b + 2 * b * c + c * d)


@_measure("eyraud")
def eyraud(a, b, c, d, n):
    return n ** 2 * (n * a - (a + b) * (a + c)) / _marginal_product(a, b, c, d)


@_measure("tarantula")
def tarantula(a, b, c, d, n):
    return a * (c + d) / (c * (a + b))


@_measure("ample")
def ample(a, b, c, d, n):
    return np.abs(a * (c + d) / (c * (a + b)))


def _mutual_information_term(p, q):
    return np.where(p > 0, p * np.log2(p / q), 0.0)


def _binary_entropy(p):
    inside = (p > 0) & (p < 1)
    return np.where(inside, -(p * np.log2(p) + (1 - p) * np.log2(1 - p)), 0.0)


@_measure("nmi")
def nmi(a, b, c, d, n):
    """Mutual information normalized by the geometric mean of the marginal entropies.

    Transcription of ``normalized_mutual_information`` from the Similarity-Measures
    repository, which follows Strehl and Ghosh (2002). By the convention of this library,
    a + c counts the presences of i and a + b those of j.
    """
    p_i = (a + c) / n
    p_j = (a + b) / n
    information = (
        _mutual_information_term(a / n, p_i * p_j)
        + _mutual_information_term(c / n, p_i * (1 - p_j))
        + _mutual_information_term(b / n, (1 - p_i) * p_j)
        + _mutual_information_term(d / n, (1 - p_i) * (1 - p_j))
    )
    return information / np.sqrt(_binary_entropy(p_i) * _binary_entropy(p_j))
