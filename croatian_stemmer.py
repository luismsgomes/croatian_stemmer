#
#    Simple stemmer for Croatian
#    Copyright 2012 Nikola Ljubešić and Ivan Pandžić
#
#    Modifications by Luís Gomes <luismsgomes@gmail.com> (May 2016) to make
#     this stemmer usable as a Python module:
#     * function hr_stem(word) => stem
#     * initialization of rules and transformations upon module import
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path
import re
import sys


__version__ = '0.1.1'


def pkg_fname(basename):
    return str(Path(__file__).with_name(basename))

def read_rules(fname):
    with open(fname) as lines:
        for line in lines:
            osnova, nastavak = line.strip().split(' ')
            yield re.compile(r'^('+osnova+')('+nastavak+r')$')

def read_transformations(fname):
    with open(fname) as lines:
        for line in lines:
            yield line.strip().split('\t')

stop = {
    'biti',
    'jesam',
    'budem',
    'sam',
    'jesi',
    'budeš',
    'si',
    'jesmo',
    'budemo',
    'smo',
    'jeste',
    'budete',
    'ste',
    'jesu',
    'budu',
    'su',
    'bih',
    'bijah',
    'bjeh',
    'bijaše',
    'bi',
    'bje',
    'bješe',
    'bijasmo',
    'bismo',
    'bjesmo',
    'bijaste',
    'biste',
    'bjeste',
    'bijahu',
    'biste',
    'bjeste',
    'bijahu',
    'bi',
    'biše',
    'bjehu',
    'bješe',
    'bio',
    'bili',
    'budimo',
    'budite',
    'bila',
    'bilo',
    'bile',
    'ću',
    'ćeš',
    'će',
    'ćemo',
    'ćete',
    'želim',
    'želiš',
    'želi',
    'želimo',
    'želite',
    'žele',
    'moram',
    'moraš',
    'mora',
    'moramo',
    'morate',
    'moraju',
    'trebam',
    'trebaš',
    'treba',
    'trebamo',
    'trebate',
    'trebaju',
    'mogu',
    'možeš',
    'može',
    'možemo',
    'možete'
}

rules = list(read_rules(pkg_fname("rules.txt")))

transformations = list(read_transformations(pkg_fname("transformations.txt")))


def istakniSlogotvornoR(niz):
    return re.sub(r'(^|[^aeiou])r($|[^aeiou])',r'\1R\2',niz)

def imaSamoglasnik(niz):
    if re.search(r'[aeiouR]',istakniSlogotvornoR(niz)) is None:
        return False
    else:
        return True

def transformiraj(pojavnica):
    for trazi,zamijeni in transformations:
        if pojavnica.endswith(trazi):
            return pojavnica[:-len(trazi)]+zamijeni
    return pojavnica

def korjenuj(pojavnica):
    for pravilo in rules:
        dioba=pravilo.match(pojavnica)
        if dioba is not None:
            if imaSamoglasnik(dioba.group(1)) and len(dioba.group(1))>1:
                return dioba.group(1)
    return pojavnica

def hr_stem(word):
    if not re.match(r'^\w+$', word) or word.lower() in stop:
        return word
    stem = korjenuj(transformiraj(word.lower()))
    if word.isupper():
        return stem.upper()
    if stem.istitle():
        return stem.title()
    return stem


def main():
    if len(sys.argv) != 1:
        sys.exit('{} takes no arguments'.format(sys.argv[0]))
    for line in sys.stdin:
        print(*[hr_stem(word) for word in line.split()])


if __name__ == '__main__':
    main()
