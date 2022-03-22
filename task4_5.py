command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

x=(command1[command1.find("vlan")+5:])
x1=(set((x.split(","))))

y=(command2[command2.find("vlan")+5:])
y1=(set((y.split(","))))

z=list(x1.union(y1))
print(z)
1
