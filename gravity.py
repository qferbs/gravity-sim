import mvector

class Mass:
    def __init__(self, mass, xyz, v0=(0, 0, 0)):
        self.mass = mass
        self.pos = xyz
        self.v = mvector.Vector(v0)
    
    def get_force(self, xyz, mass1):
        r = mvector.Vector(mvector.add_vector(xyz, mvector.scale_vector(self.pos, -1)))
        r_unit = mvector.scale_vector(r.xyz(), 1/r.magnitude())
        force = mvector.scale_vector(r_unit, -self.mass*mass1 / (r.magnitude()**2))
        return force

    def update_pos(self, dt, a=(0, 0, 0)):
        self.v.set_xyz(mvector.add_vector(self.v.xyz(), mvector.scale_vector(a, dt/1000)))
        self.pos = mvector.add_vector(self.pos, mvector.scale_vector(self.v.xyz(), dt/1000))

def update(masses, dt):
    m_accels = {}
    for mass in masses:
        Fnet = (0, 0, 0)
        for m in [j for j in masses if j is not mass]:
            f = m.get_force(mass.pos, mass.mass)
            Fnet = mvector.add_vector(Fnet, f)
        m_accels[mass] = Fnet

    for mass in masses:
        mass.update_pos(dt, mvector.scale_vector(m_accels[mass], 1/mass.mass))
