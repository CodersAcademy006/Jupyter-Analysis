import plotly.graph_objects as go

def plot_patient_flow_sankey(df):
    """Plot Sankey diagram for patient flow."""
    # Example assumes columns: 'admission_source', 'icu_type', 'discharge_status'
    sources = df['admission_source']
    targets = df['icu_type']
    values = df.groupby(['admission_source', 'icu_type']).size().values
    fig = go.Figure(go.Sankey(
        node=dict(label=list(set(sources) | set(targets))),
        link=dict(source=[list(set(sources) | set(targets)).index(s) for s in sources],
                  target=[list(set(sources) | set(targets)).index(t) for t in targets],
                  value=values)
    ))
    fig.show()
