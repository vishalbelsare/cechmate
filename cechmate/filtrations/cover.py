"""

    Implementation of the Cover filtration from a cover.

    The Cover filtration is built from a cover by using the Jaccard Distance as birth times for the simplex. 


"""
import itertools

from .base import BaseFiltration

"""
    TODO: Build the Cech filtration that can be built using any metric.
    
    Can the Jaccard Filtration be built from this?

"""

class Cech(BaseFiltration):

    def metric(self, elems):
        pass

class Cover(BaseFiltration):
    def jaccard(self, covers):
        """ Jaccard Distance 
        """
        covers_as_sets = list(map(set, covers))
        intersection = set.intersection(*covers_as_sets)
        union = set.union(*covers_as_sets)

        return 1 - len(intersection) / len(union)
    
    def build(self, covers):

        # Give each cover element a name.
        if not isinstance(covers, dict):
            covers = dict(enumerate(covers))

        simplices = [([k], 0.0) for k in covers.keys()]

        # TODO: be more intelligent about which combos we check

        for k in range(2, self.max_dim + 2):
            for potentials in itertools.combinations(covers.keys(), k):
                potential_sets = [covers[p] for p in potentials]

                d = self.jaccard(potential_sets)

                # TODO: Do we want to include all of these simplices as well?
                if d < 1:
                    simplices.append((potentials, d))

        return simplices

__all__ = ["Cover"]