"""
Copyright 2017 Nikolay Stanchev

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import unittest

from ADTs.AbstractDataStructures import PriorityQueue


class PriorityQueueTest(unittest.TestCase):

    def test_size(self):
        priority_queue = PriorityQueue()
        self.assertEqual(len(priority_queue), 0, "Priority queue is not initialised as empty")
        priority_queue = PriorityQueue(float, True)
        self.assertEqual(priority_queue.size(), 0, "Priority queue is not initialised as empty")
        priority_queue = PriorityQueue(elements_type=int, reverse=False)
        self.assertEqual(len(priority_queue), 0, "Priority queue is not initialised as empty")
        self.assertTrue(priority_queue.is_empty(), "Priority queue is not initialised as empty")
        self.assertEqual(priority_queue.size(), 0, "Priority queue is not initialised as empty")

        priority_queue.enqueue(5, 10)
        priority_queue.enqueue(20, 3)
        self.assertEqual(priority_queue.size(), 2, "Wrong size implementation")
        self.assertEqual(len(priority_queue), 2, "Wrong len implementation")

        priority_queue = PriorityQueue(reverse=False)
        priority_queue.enqueue(20, 3)
        priority_queue.peek()
        priority_queue.enqueue(2, 2)
        priority_queue.enqueue(10, 3)
        self.assertEqual(priority_queue.size(), 2, "Wrong size implementation")

        priority_queue.dequeue()
        priority_queue.get(1024)
        self.assertEqual(len(priority_queue), 1, "Wrong len implementation")

    def test_type(self):
        with self.assertRaises(TypeError):
            priority_queue = PriorityQueue(elements_type=5.4)

        priority_queue = PriorityQueue()
        self.assertEqual(priority_queue.type(), None, "Wrong type at initialization")
        priority_queue.enqueue(5, 5)
        priority_queue.enqueue("word", 10)
        priority_queue = PriorityQueue(str, True)
        self.assertEqual(priority_queue.type(), str, "Wrong type at initialization")

        with self.assertRaises(TypeError):
            priority_queue.enqueue(2, 3)

        with self.assertRaises(TypeError):
            priority_queue.enqueue("2", "3")

        with self.assertRaises(TypeError):
            priority_queue.contains(5.43)

        with self.assertRaises(TypeError):
            priority_queue.get("7")

    def test_reverse(self):
        priority_queue = PriorityQueue()
        self.assertFalse(priority_queue.is_reversed(), "Wrong reverse implementation")
        priority_queue.enqueue(1, 10)
        priority_queue.enqueue("word", 5)
        self.assertEqual(priority_queue.peek(), 1, "Wrong reverse implementation")
        self.assertEqual(priority_queue.dequeue(), 1, "Wrong reverse implementation")

        priority_queue = PriorityQueue(int, False)
        self.assertFalse(priority_queue.is_reversed(), "Wrong reverse implementation")
        priority_queue.enqueue(1, 10)
        priority_queue.enqueue(2, 5)
        self.assertEqual(priority_queue.peek(), 1, "Wrong reverse implementation")
        self.assertEqual(priority_queue.dequeue(), 1, "Wrong reverse implementation")

        priority_queue = PriorityQueue(elements_type=str, reverse=True)
        self.assertTrue(priority_queue.is_reversed(), "Wrong reverse implementation")
        priority_queue.enqueue("python", 1)
        priority_queue.enqueue("word", 2)
        self.assertEqual(priority_queue.peek(), "python", "Wrong reverse implementation")
        self.assertEqual(priority_queue.dequeue(), "python", "Wrong reverse implementation")

        priority_queue = PriorityQueue(reverse=True)
        self.assertTrue(priority_queue.is_reversed(), "Wrong reverse implementation")

        priority_queue.enqueue(1, 10)
        priority_queue.enqueue("word", 5)
        self.assertEqual(priority_queue.peek(), "word", "Wrong reverse implementation")
        self.assertEqual(priority_queue.dequeue(), "word", "Wrong reverse implementation")

    def test_str(self):
        priority_queue = PriorityQueue()
        self.assertEqual(str(priority_queue), "{}", "Wrong str implementation")
        priority_queue = PriorityQueue(float, True)
        self.assertEqual(str(priority_queue), "{}", "Wrong str implementation")

    def test_contains(self):
        priority_queue = PriorityQueue()
        self.assertFalse(5 in priority_queue, "Contains fails with empty queue")
        with self.assertRaises(TypeError):
            priority_queue.contains("7")

        self.assertFalse(priority_queue.contains_element("7"), "Contains_element fails")

        priority_queue = PriorityQueue(int, True)
        for i in range(10):
            priority_queue.enqueue(i**2, i)

        for j in range(10):
            self.assertTrue(j in priority_queue, "Wrong contains impementation")
            self.assertTrue(priority_queue.contains_element(j**2), "Contains_element fails")

        with self.assertRaises(TypeError):
            priority_queue.contains_element("word")

    def test_enqueue(self):
        priority_queue = PriorityQueue(float, False)
        with self.assertRaises(TypeError):
            priority_queue.enqueue(5, 5)
        with self.assertRaises(TypeError):
            priority_queue.enqueue(5.25, "5")

        d = {5: 10.5, 1: 2.7, 3: 4.90, 11: 3.14}
        for key in d:
            priority_queue.enqueue(d[key], key)

        self.assertEqual(len(priority_queue), len(d))

        for priority in d:
            self.assertFalse(priority_queue.get(priority) is None)
            self.assertEqual(d[priority], priority_queue.get(priority))

    def test_dequeue(self):
        priority_queue = PriorityQueue(str, True)
        with self.assertRaises(ValueError):
            priority_queue.dequeue()
        priority_queue.enqueue("word", 2)
        priority_queue.enqueue("python", 10)
        priority_queue.enqueue("another_word", 1)
        self.assertEqual(priority_queue.dequeue(), "another_word", "Wrong dequeue implementation")
        self.assertEqual(len(priority_queue), 2)

        priority_queue = PriorityQueue(int, False)
        with self.assertRaises(ValueError):
            priority_queue.dequeue()
        priority_queue.enqueue(15, 2)
        priority_queue.enqueue(423, 10)
        priority_queue.enqueue(20, 1)
        self.assertEqual(priority_queue.dequeue(), 423, "Wrong dequeue implementation")
        self.assertEqual(priority_queue.dequeue(), 15, "Wrong deuque implementation")
        self.assertEqual(len(priority_queue), 1)

    def test_iterator(self):
        priority_queue = PriorityQueue()
        with self.assertRaises(StopIteration):
            iter(priority_queue).__next__()

        for p in range(0, 41, 2):
            priority_queue.enqueue(p*2, p)

        list2 = [p*2 for p in range(0, 41, 2)]

        for value in priority_queue:
            self.assertTrue(value in list2, "Wrong iterator implementation")
            self.assertEqual(value, max(list2))
            list2.remove(value)
        self.assertEqual(len(priority_queue), 0)
        self.assertTrue(priority_queue.is_empty())

    def test_peek(self):
        priority_queue = PriorityQueue()
        self.assertTrue(priority_queue.peek() is None, "Wrong peek implementation")
        priority_queue = PriorityQueue(float, True)
        self.assertTrue(priority_queue.peek() is None, "Wrong peek implementation")

        priority_queue.enqueue(15.25, 2)
        priority_queue.enqueue(423.56, 10)
        priority_queue.enqueue(20.02, 1)
        priority_queue.enqueue(33.5, 5)
        self.assertEqual(priority_queue.peek(), 20.02, "Wrong dequeue implementation")
        self.assertEqual(priority_queue.dequeue(), 20.02, "Wrong dequeue implementation")
        self.assertEqual(priority_queue.peek(), 15.25, "Wrong deuque implementation")
        self.assertEqual(len(priority_queue), 3)

    def test_get(self):
        priority_queue = PriorityQueue()
        for k in range(10):
            self.assertTrue(priority_queue.get(k) is None, "Wrong get implementation")
            priority_queue.enqueue(k*3, k)

        for n in range(9, -1, -1):
            self.assertEqual(priority_queue.get(n), n*3, "Wrong peek implementation")

        self.assertEqual(len(priority_queue), 10)
