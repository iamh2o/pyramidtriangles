from pytest import raises

from color import Color
from grid import (
    Position, Geometry, Cell, Address, bottom_edge, left_edge, right_edge, vertex_neighbors, edge_neighbors,
    Coordinate, Face, Panel, Universe
)
from model import ModelBase


class FakeModel(ModelBase):
    def set(self, cell: Cell, addr: Address, color: Color):
        pass

    def go(self):
        pass


def single_panel_grid(rows):
    geom = Geometry(origin=Coordinate(0, 0), rows=rows)
    return Face(FakeModel(),
                geom,
                [Panel(geom, Address(Universe(1, 1), 4))])


def test_triangle_counts():
    for row_count in range(1, 15):
        triangle = single_panel_grid(row_count)
        assert triangle.row_count == row_count

        expected_cell_count = Geometry.triangular_number(row_count)
        assert len(triangle) == len(triangle.cells) == expected_cell_count,\
            f'cell count {len(triangle.cells)} != expected {expected_cell_count} with rows {row_count}'

        # Each edge has the same number of elements are the number or total rows.
        assert row_count == len(bottom_edge(triangle)) == len(
            left_edge(triangle)) == len(right_edge(triangle))


def test_cells_out_of_bounds():
    triangle = single_panel_grid(2)

    with raises(KeyError):
        triangle[Coordinate(-1, 0)]
    with raises(KeyError):
        triangle[Coordinate(0, -1)]
    with raises(KeyError):
        triangle[Position(0, 1)]  # Only (0, 0) in first row.
    with raises(KeyError):
        triangle[Position(1, 3)]
    with raises(KeyError):
        triangle[Position(2, 0)]  # Row 2 does not exist.

    with raises(TypeError):
        triangle[1]


def test_cell_attributes():
    triangle = single_panel_grid(3)
    assert len(triangle.cells) == 9

    top = triangle[Position(0, 0)]
    assert top.is_top_corner and top.is_left_edge and top.is_right_edge and top.is_up and top.is_edge
    assert not top.is_bottom_edge

    left_corner = triangle[Position(2, 0)]
    assert left_corner.is_left_corner and left_corner.is_left_edge and left_corner.is_bottom_edge and left_corner.is_up
    assert not left_corner.is_right_edge

    right_corner = triangle[Position(2, 4)]
    assert right_corner.is_right_corner and right_corner.is_right_edge and right_corner.is_bottom_edge
    assert right_corner.is_up
    assert not right_corner.is_left_edge

    inner = triangle[Position(1, 1)]
    assert inner.is_down
    assert not inner.is_left_edge and not inner.is_right_edge and not inner.is_bottom_edge and not inner.is_edge


def test_cell_neighbors():
    triangle = single_panel_grid(5)

    # TODO: remove cell ID checks

    # Upward facing cell
    (left, middle, right) = triangle.select(edge_neighbors(Position(2, 2)))
    assert left.id == 5
    assert middle.id == 12
    assert right.id == 7

    (left, middle, right) = triangle.select(vertex_neighbors(Position(2, 2)))
    assert left.id == 10
    assert middle.id == 2
    assert right.id == 14

    # Downward facing cell
    (left, middle, right) = triangle.select(edge_neighbors(Position(2, 1)))
    assert left.id == 4
    assert middle.id == 1
    assert right.id == 6

    (left, middle, right) = triangle.select(vertex_neighbors(Position(2, 1)))
    assert not left.real
    assert middle.id == 11
    assert right.id == 3

    # Invalid cell
    assert not any(triangle.select(edge_neighbors(Position(1, -1))))
    assert not any(triangle.select(vertex_neighbors(Position(1, -1))))
