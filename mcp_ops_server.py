
import sqlite3
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    from mcp.server.mcpserver import MCPServer as FastMCP

mcp = FastMCP("OperationsDataServer")

def _query_db(query: str, params: tuple = ()) -> list[dict]:
    conn = sqlite3.connect("ops_company.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, params)
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

@mcp.tool()
def get_regional_sales(quarter: str = "Q3") -> list[dict]:
    """Consulta ingresos reales, objetivo en euros y plantilla por región en un trimestre."""
    return _query_db(
        "SELECT region, quarter, revenue_eur, target_eur, headcount FROM regional_sales WHERE quarter = ?",
        (quarter,),
    )

@mcp.tool()
def get_hardware_catalog() -> list[dict]:
    """Consulta el catálogo de equipamiento disponible, su precio unitario y el stock actual."""
    return _query_db("SELECT sku, item_name, unit_price_eur, stock FROM hardware_catalog")

if __name__ == "__main__":
    mcp.run()
