from basicos_python.Ejercicio42.main import area_circle, volume_cilinder

def test_area_circle_positive():
    assert area_circle(1)=="3.14"
    assert area_circle(5)=="78.54"
    assert area_circle(10)== "314.16"

def test_limit_numbers():
    assert area_circle(0)==None
    assert area_circle(-1)==None
    assert volume_cilinder(0,10)==None
    assert volume_cilinder(-1.5,3)==None
    assert volume_cilinder(-1.5,120)==None

def test_volume_cilinder_positive():
    assert volume_cilinder(4,10)=="502.65"
    assert volume_cilinder(0.5,2)=="1.57"
    assert volume_cilinder(1.5,3)== "21.21"
    