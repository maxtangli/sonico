#include <map>
#include <set>

int main() {
    // sorted by key, typically implemented by red-black tree, a kind of self-balancing binary search tree.
    std::map<int, int> m;
//    class Compare = std::less<Key> // invoke operator< on type Key. for custom-type key, define operator<.
//    class Allocator = std::allocator<std::pair<const Key, T> >

    // insert: O(log n)
    // find: O(log n)

    // set is like a map without value.
    std::set<int> s;

    // multi: variant allowing duplicated keys, e.g. multimap, multiset.
    // unordered: variant not sorted, implemented by hash, e.g. unordered_map, unordered_set, unordered_multimap, unordered_multiset.

    return 0;
}