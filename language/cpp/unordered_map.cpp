#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cassert>

/**
 * unordered_map
 * - [x] basic
 * - [x] bucket and performance
 * - [x] custom type key
 */

typedef std::unordered_map<int, int> dict;
// Hash = std::hash<Key> // for custom-type key, inject std::hash<custom-type>
// KeyEqual = std::equal_to<Key>, // invoke operator== on type T. for custom-type key, define operator==.
// Allocator = std::allocator< std::pair<const Key, T> >

void test_basic() {
    // init
    dict u = {{1, 10},
              {2, 20},
              {3, 30}};

    // find(key): O(1 - n), hash(key) -> bucket -> iterate the bucket
    u.at(1); // find or exception
    auto iter = u.find(0); // find or end()

    // iterate to find: O(n)
    auto iter2 = std::find_if(u.begin(), u.end(), [](dict::const_reference kvp) -> bool { return kvp.first == 0; });
    assert(iter == iter2);

    // update: O(1 - n), hash(key) -> bucket -> iterate the bucket
    auto result = u.insert({3, 33}); // find or insert
    assert(u[3] == 30);

    u[3] = 33; // override or insert
    ++u[0];
    assert(u[3] == 33);
    assert(u[0] == 1);

    u.erase(0);
    assert(u.find(0) == u.end());

    // loop: undefined order
    for (const auto &kvp : u) {
        std::cout << kvp.first << "," << kvp.second << "]\n";
    }

    std::for_each(u.begin(), u.end(),
                  [](dict::const_reference kvp) { std::cout << kvp.first << "," << kvp.second << "]\n"; });

    // copy to vector
    typedef std::vector<std::pair<int, int>> myvector;
    myvector vec;
    std::copy(u.begin(), u.end(), std::back_inserter(vec));
    std::for_each(vec.begin(), vec.end(),
                  []( myvector::const_reference kvp) { std::cout << kvp.first << "," << kvp.second << "]\n"; });


    std::cout << "done.\n";
}

void test_bucket() {
    auto echo = [](const dict &u) {
        std::cout << u.size() << " entry, "
                  << u.bucket_count() << " bucket, "
                  << u.load_factor() << "/" << u.max_load_factor() << " load_factor.\n";
    };

    dict u;
//    u.reserve(100000); // to avoid rehash, pre-allocate buckets with capacity of 100000 elements
    echo(u);

    auto should_echo = [](const dict &u, dict::size_type &pre_bucket_count) {
        auto current_bucket_count = u.bucket_count();
        bool changed = (current_bucket_count != pre_bucket_count);
        pre_bucket_count = current_bucket_count;
        return changed;
    };
    auto pre_bucket_count = u.bucket_count();
    for (int i = 0; i < 100000; ++i) {
        u[i] = i;
        if (should_echo(u, pre_bucket_count)) {
            echo(u);
        }
    }

    for (int i = 0; i < 100000; ++i) {
        u.erase(i);
        if (should_echo(u, pre_bucket_count)) {
            echo(u);
        }
    }

    std::cout << "done.\n";

    /**
     * init()
     *  bucket_count = 1, max_load_factor = 1
     *
     * onSizeChanged(size)
     *  load_factor = size / bucket_count
     *  if load_factor >= max_load_factor
     *   new_bucket_count = bucket_count * 2 + ?
     *   rehash(new_bucket_count)
     *
     * rehash(new_bucket_count which > bucket_count)
     *  allocate new bucket
     *  move all elements to proper bucket
     */
}

class custom_key {
public:
    int id;
    int sub_id;

    custom_key(int id, int sub_id) : id(id), sub_id(sub_id) {}

    bool operator==(const custom_key &rhs) const;

    bool operator!=(const custom_key &rhs) const;
};

bool custom_key::operator==(const custom_key &rhs) const {
    return id == rhs.id &&
           sub_id == rhs.sub_id;
}

bool custom_key::operator!=(const custom_key &rhs) const {
    return !(rhs == *this);
}

namespace std {
    template<>
    struct hash<custom_key> {
        std::size_t operator()(custom_key const &s) const {
            std::size_t const h1(std::hash<int>{}(s.id));
            std::size_t const h2(std::hash<int>{}(s.sub_id));
            return h1 ^ (h2 << 1); // or use boost::hash_combine (see Discussion)
        }
    };
}

void test_custom_key() {
    std::unordered_map<custom_key, int> m;
    custom_key key(1, 0);
    m[key] = 10;
    std::cout << m[key] << "\n";

    std::cout << "done.\n";
}

int main() {
    test_basic();
//    test_bucket();
//    test_custom_key();

    return 0;
}