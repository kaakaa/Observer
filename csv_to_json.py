#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, codecs
import csv

class Node:
	def __init__(self, name, value):
		self.name = name
		self.size = value
		self.children = []
 
	def has_child(self, name):
		for child in self.children:
			if(child.name == name):
				return True
		return False
 
	def add_child(self, name, value):
		if(not self.has_child(name)):
			child = Node(name, value)
			self.children.append(child)
 
	def transform(self):
		child_nodes = []
		if(len(self.children) == 0):
			return {
				"name" : self.name,
				"size" : self.size
			}
		else:
			for child in self.children:
				child_nodes.append(child.transform())
			return {
				"name":self.name,
				"children":child_nodes
			}
 
def make_node(row,nodes):
	origin = nodes
	list = row[0].split('\\')
	value = row[1]
	for i in range(0,len(list)):
		nodes.add_child(list[i],value)
		for child in nodes.children:
			if(child.name == list[i]):
				nodes = child
	return origin


f = codecs.open(r"D:\TracLight\CollabNetSVN\httpd\htdocs\update_observer\update.csv", "r", "sjis")
csv = csv.reader(f)
nodes = Node("root", 0)
for row in csv:
	nodes = make_node(row,nodes)
 
out = nodes.transform()
 
f = codecs.open(r"D:\TracLight\CollabNetSVN\httpd\htdocs\update_observer\flare.json", "w", "utf-8")
json.dump(out, f, indent=2, sort_keys=True, ensure_ascii=False)
f.close()
